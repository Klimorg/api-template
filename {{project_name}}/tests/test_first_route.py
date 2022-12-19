import json

import jsonschema
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_post_first_route():

    payload = {
        "inference_date": "2022-12-17",
        "inference_time": "16:56:26",
        "num": 0,
    }

    response = client.post("/first_route/", json=payload)

    assert response.status_code == 201

    response = response.json()

    with open("tests/jsons/base-create-output.schema.json") as schema:
        response_schema = json.load(schema)
        jsonschema.validate(response, response_schema)


def test_get_first_route():

    response = client.get("/first_route/")

    assert response.status_code == 200

    response = response.json()

    with open("tests/jsons/base-read.schema.json") as schema:
        response_schema = json.load(schema)
        jsonschema.validate(response, response_schema)