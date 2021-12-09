import json
from pathlib import Path
from time import sleep
from typing import List

import pytest
import shortuuid
from httpx import BasicAuth
from httpx import Client as HttpxClient

from sherpa_client.api.documents import launch_document_import, export_documents_sample, get_document
from sherpa_client.api.jobs import get_job
from sherpa_client.api.projects import get_projects, create_project, delete_project, get_project_info
from sherpa_client.client import Client
from sherpa_client.models import Credentials, ProjectConfigCreation, ProjectStatus, ProjectBean, SherpaJobBeanStatus, \
    SherpaJobBean, LaunchDocumentImportMultipartData, Document
from sherpa_client.types import File


@pytest.fixture(autouse=True, scope="session")
def client():
    testdir = Path(__file__).parent / "data"
    json_file = testdir / "credentials.json"
    with json_file.open("r") as fin:
        creds = json.load(fin)
        url = creds.pop("url")
        creds = Credentials.from_dict(creds)
        httpx_client = HttpxClient(base_url=url,
                                   auth=BasicAuth(username=creds.email, password=creds.password),
                                   headers={"User-Agent": "sherpa-client/0.9.21"})
        res = httpx_client.get("/users", params={'username': creds.email})
        if res.is_success:
            client = Client(base_url=url, timeout=300, cookies=res.cookies)
            yield client


def is_success(job_bean):
    return job_bean and job_bean.status == SherpaJobBeanStatus.COMPLETED


@pytest.fixture(autouse=True, scope="session")
def project(client):
    shortuuid.set_alphabet('123456789abcdefghijkmnopqrstuvwxyz_')
    pname = "test_" + shortuuid.uuid()[:12]
    r = create_project.sync_detailed(client=client,
                                     json_body=ProjectConfigCreation(name=pname, label="SHERPA-CLIENT",
                                                                     description="Test project for sherpa-client"))
    # setup_stuff
    if r.is_success:
        project_status: ProjectStatus = r.parsed
        job_bean = wait_for_completion(project_status.pending_job, client=client)
        if project_status.status == 'created' or is_success(job_bean):
            yield project_status.project_name
    # teardown_stuff
    ack = delete_project.sync(pname, client=client)
    pass


def wait_for_completion(job_bean: SherpaJobBean, client=client):
    if job_bean:
        while job_bean.status not in [SherpaJobBeanStatus.COMPLETED,
                                      SherpaJobBeanStatus.CANCELLED,
                                      SherpaJobBeanStatus.FAILED]:
            sleep(10)
            job_bean = get_job.sync(job_bean.project,
                                    job_bean.id, client=client)
    return job_bean


def test_login(client):
    assert client.cookies is not None
    assert 'vertx-web.session' in client.cookies


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
    with json_file.open("r") as fin:
        multipart_data = LaunchDocumentImportMultipartData(
            file=File(file_name=json_file.name, payload=fin, mime_type="application/json"))
        r = launch_document_import.sync_detailed(project, client=client,
                                                 multipart_data=multipart_data)
        if r.is_success:
            job_bean: SherpaJobBean = r.parsed
            job_bean = wait_for_completion(job_bean, client=client)
            if is_success(job_bean):
                assert 'Importing' in job_bean.description
                assert '1 documents' in job_bean.status_message


def test_export_documents_sample(client, project):
    r = export_documents_sample.sync_detailed(project, client=client,
                                              sample_size=1)
    if r.is_success:
        docs: List[Document] = r.parsed
        assert len(docs) == 1
        assert docs[0].text
        assert docs[0].identifier == 'a01'
        assert docs[0].title == 'a01'


def test_get_document(client, project):
    r = get_document.sync_detailed(project, 'a01', client=client)
    if r.is_success:
        doc: Document = r.parsed
        assert doc.text
        assert doc.identifier == 'a01'
        assert doc.title == 'a01'
        assert len(doc.sentences) == 20
        assert len(doc.annotations) == 27
