import sys
from http import HTTPStatus

from fastapi.testclient import TestClient

# FastAPI test suite uses requests underneath.
from requests.auth import HTTPBasicAuth

from src import main

client = TestClient(main.app)


def test_auth_error():
    response = client.get("/greetings")
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not authenticated"}


def test_ok():
    response = client.get(
        "/greetings", verify=False, auth=HTTPBasicAuth("ubuntu", "debian")
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "ok": True,
        "status_code": HTTPStatus.OK,
        "message": "Hello from Fly!",
        "python_version": sys.version,
    }
