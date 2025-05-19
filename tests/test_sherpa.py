import json
from pathlib import Path
from time import sleep
from typing import List

import pytest
import shortuuid
from httpx import BasicAuth

from sherpa_client import ApiKeyAuth, AuthenticatedClient
from sherpa_client.api.annotate import annotate_text_with_project_annotator
from sherpa_client.api.authentication import user_sign_out
from sherpa_client.api.documents import (
    export_documents_sample,
    get_document,
    launch_document_import,
)
from sherpa_client.api.experiments import get_experiments, launch_experiment
from sherpa_client.api.gazetteers import create_gazetteer, synchronize_gazetteer
from sherpa_client.api.jobs import get_job
from sherpa_client.api.labels import create_label
from sherpa_client.api.lexicons import (
    create_lexicon,
    create_term,
    delete_terms_by_lexicon_name,
    get_lexicon,
)
from sherpa_client.api.plans import create_plan
from sherpa_client.api.projects import (
    create_project,
    delete_project,
    get_project_info,
    get_projects,
)
from sherpa_client.models import (
    AnnotatedDocument,
    AnnotationPlan,
    CreateLexiconResponse200,
    CreateTermBody,
    CreateTermResponse200,
    Credentials,
    Document,
    EngineName,
    Experiment,
    Label,
    LaunchDocumentImportBody,
    Lexicon,
    NewGazetteer,
    NewGazetteerParameters,
    NewNamedAnnotationPlan,
    PartialLabel,
    PartialLexicon,
    ProjectBean,
    ProjectConfigCreation,
    ProjectStatus,
    SherpaJobBean,
    SherpaJobBeanStatus,
    WithAnnotator,
)
from sherpa_client.types import File


@pytest.fixture(autouse=True, scope="session")
def client():
    testdir = Path(__file__).parent / "data"
    json_file = testdir / "credentials.json"
    with json_file.open("r") as fin:
        creds = json.load(fin)
        url = creds.pop("url")
        creds = Credentials.from_dict(creds)
        # client = Client(base_url=url, timeout=300, httpx_args={"auth": BasicAuth(username=creds.email, password=creds.password)})
        client = AuthenticatedClient(
            base_url=url,
            timeout=300,
            auth=BasicAuth(username=creds.email, password=creds.password),
        )
        res = client.get_httpx_client().get("/current_user")
        if not res.is_success:
            res.raise_for_status()
        yield client
    # teardown_stuff
    ack = user_sign_out.sync_detailed(client=client)


@pytest.fixture(autouse=True, scope="session")
def apikey_client():
    testdir = Path(__file__).parent / "data"
    json_file = testdir / "credentials.json"
    with json_file.open("r") as fin:
        creds = json.load(fin)
        url = creds.pop("url")
        key = creds.pop("key")
        client = AuthenticatedClient(base_url=url, timeout=300, auth=ApiKeyAuth(key))
        res = client.get_httpx_client().get("/current_user")
        if not res.is_success:
            res.raise_for_status()
        # setup_stuff
        yield client
    # teardown_stuff
    ack = user_sign_out.sync_detailed(client=client)


def is_success(job_bean):
    return job_bean and job_bean.status == SherpaJobBeanStatus.COMPLETED


@pytest.fixture(autouse=True, scope="session")
def project(client):
    shortuuid.set_alphabet("123456789abcdefghijkmnopqrstuvwxyz_")
    pname = "test_" + shortuuid.uuid()[:12]
    r = create_project.sync_detailed(
        client=client,
        body=ProjectConfigCreation(
            name=pname,
            label="SHERPA-CLIENT",
            description="Test project for sherpa-client",
        ),
        group_name="kairntech",
    )
    # setup_stuff
    if r.is_success:
        project_status: ProjectStatus = r.parsed
        job_bean = wait_for_completion(project_status.pending_job, client=client)
        if project_status.status == "created" or is_success(job_bean):
            yield project_status.project_name
    # teardown_stuff
    ack = delete_project.sync(pname, client=client)


def wait_for_completion(job_bean: SherpaJobBean, client=client):
    if job_bean:
        while job_bean.status not in [
            SherpaJobBeanStatus.COMPLETED,
            SherpaJobBeanStatus.CANCELLED,
            SherpaJobBeanStatus.FAILED,
        ]:
            sleep(10)
            job_bean = get_job.sync(job_bean.project, job_bean.id, client=client)
    return job_bean


def test_login_with_token(client):
    assert "vertx-web.session" in client.get_httpx_client().cookies


def test_login_with_apikey(apikey_client):
    assert apikey_client.auth is not None
    assert apikey_client.auth.token is not None
    assert apikey_client.auth.api_key_header_name is not None
    r = get_projects.sync_detailed(client=apikey_client)
    assert r.is_success


def test_get_project_info(client, project):
    r = get_project_info.sync_detailed(project, client=client)
    if r.is_success:
        result: ProjectBean = r.parsed
        assert result is not None
        assert project == result.name


def test_get_projects(client, project):
    r = get_projects.sync_detailed(client=client)
    if r.is_success:
        result: List[ProjectBean] = r.parsed
        assert result is not None
        pnames = [p.name for p in result]
        assert project in pnames


def test_import_documents(client, project):
    testdir = Path(__file__).parent / "data"
    json_file = testdir / "20_dummy_segs_with_annotations.json"
    with json_file.open("rb") as fin:
        multipart_data = LaunchDocumentImportBody(
            file=File(
                file_name=json_file.name, payload=fin, mime_type="application/json"
            )
        )
        r = launch_document_import.sync_detailed(
            project, client=client, body=multipart_data
        )
        if r.is_success:
            job_bean: SherpaJobBean = r.parsed
            job_bean = wait_for_completion(job_bean, client=client)
            if is_success(job_bean):
                assert "Importing" in job_bean.description
                assert "1 documents" in job_bean.status_message


def test_get_document(client, project):
    r = get_document.sync_detailed(project, "a01", client=client)
    if r.is_success:
        doc: Document = r.parsed
        assert doc.text
        assert doc.identifier == "a01"
        assert doc.title == "a01"
        assert len(doc.sentences) == 20
        assert len(doc.annotations) == 20


def test_export_documents_sample(client, project):
    r = export_documents_sample.sync_detailed(project, client=client, sample_size=1)
    if r.is_success:
        docs: List[Document] = r.parsed
        assert len(docs) == 1
        assert docs[0].text
        assert docs[0].identifier == "a01"
        assert docs[0].title == "a01"


def test_get_experiments(client, project):
    r = get_experiments.sync_detailed(project, client=client)
    if r.is_success:
        exps: List[Experiment] = r.parsed
        assert len(exps) > 1
        exp0 = exps[0]
        assert exp0.label == "CRFSuite"


def test_train_experiment(client, project):
    r = launch_experiment.sync_detailed(project, "crfsuite", client=client)
    if r.is_success:
        job_bean: SherpaJobBean = r.parsed
        job_bean = wait_for_completion(job_bean, client=client)
        if is_success(job_bean):
            assert "CRFSuite experiment" in job_bean.description
            assert "done in" in job_bean.status_message


def test_annotate_with_experiment(client, project):
    r = annotate_text_with_project_annotator.sync_detailed(
        project, "crfsuite", client=client, body="This is a test99"
    )
    if r.is_success:
        doc: AnnotatedDocument = r.parsed
        assert len(doc.annotations) == 1
        assert doc.annotations[0].text == "test99"


def test_create_lexicon_and_gazetteer(client, project):
    r = create_lexicon.sync_detailed(
        project, client=client, body=PartialLexicon(label="lex")
    )
    if r.is_success:
        res: CreateLexiconResponse200 = r.parsed
        r = create_term.sync_detailed(
            project,
            "lex",
            client=client,
            body=CreateTermBody.from_dict({"identifier": "This"}),
        )
        if r.is_success:
            res: CreateTermResponse200 = r.parsed
            r = create_label.sync_detailed(
                project,
                client=client,
                body=PartialLabel(label="Term", name="term"),
            )
            if r.is_success:
                lab: Label = r.parsed
                r = create_gazetteer.sync_detailed(
                    project,
                    client=client,
                    body=NewGazetteer(
                        engine="PhraseMatcher",
                        label="Gaz",
                        parameters=NewGazetteerParameters.from_dict(
                            {"parameters": {"terms": {"term": "lex"}}}
                        ),
                    ),
                )
                if r.is_success:
                    eng: EngineName = r.parsed
                    r = synchronize_gazetteer.sync_detailed(
                        project, eng.name, client=client
                    )
                    if r.is_success:
                        job_bean: SherpaJobBean = r.parsed
                        job_bean = wait_for_completion(job_bean, client=client)
                        if is_success(job_bean):
                            assert "terms synchronization" in job_bean.description
                            assert "done in" in job_bean.status_message


def test_annotate_with_gazetteer(client, project):
    r = annotate_text_with_project_annotator.sync_detailed(
        project, "gaz", client=client, body="This is a test99"
    )
    if r.is_success:
        doc: AnnotatedDocument = r.parsed
        assert len(doc.annotations) == 1
        assert doc.annotations[0].text == "This"


def test_create_plan(client, project):
    r = create_plan.sync_detailed(
        project,
        client=client,
        body=NewNamedAnnotationPlan(
            label="Plan",
            parameters=AnnotationPlan(
                pipeline=[
                    WithAnnotator(annotator="crfsuite"),
                    WithAnnotator(annotator="gaz"),
                ]
            ),
        ),
    )
    if r.is_success:
        eng: EngineName = r.parsed
        assert eng.name == "plan"


def test_annotate_with_plan(client, project):
    r = annotate_text_with_project_annotator.sync_detailed(
        project, "plan", client=client, body="This is a test99"
    )
    if r.is_success:
        doc: AnnotatedDocument = r.parsed
        assert len(doc.annotations) == 2
        assert doc.annotations[0].text == "This"
        assert doc.annotations[1].text == "test99"


def test_clear_lexicon(client, project):
    r = get_lexicon.sync_detailed(project, "lex", client=client, compute_metrics=True)
    if r.is_success:
        lexicon: Lexicon = r.parsed
        assert lexicon.terms > 0
    r = delete_terms_by_lexicon_name.sync_detailed(project, "lex", client=client)
    if r.is_success:
        r = get_lexicon.sync_detailed(
            project, "lex", client=client, compute_metrics=True
        )
        if r.is_success:
            lexicon: Lexicon = r.parsed
            assert lexicon.terms == 0
