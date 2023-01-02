from fastapi.testclient import TestClient
import json
import jsonschema
from app.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)


def test_read_main(client: TestClient)->None:
    response = client.get("/healthcheck/")
    assert response.status_code == 200


def test_get_last_deployment_infos(client: TestClient)->None:
    response = client.get("/last_deployment_infos/")
    assert response.status_code == 200

    response = response.json()

    with open("tests/jsons/deployment-info.schema.json") as schema:
        response_schema = json.load(schema)
        jsonschema.validate(response, response_schema)
