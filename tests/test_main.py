import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


def test_add_sheep():
    sheep_data = {
        "id": 24,
        "name": "Bessie",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=sheep_data)

    assert response.status_code == 201
    assert response.json() == sheep_data

    get_response = client.get("/sheep/24")
    assert get_response.status_code == 200
    assert get_response.json() == sheep_data


def test_update_sheep():
    updated_data = {
        "id": 1,
        "name": "Spice Updated",
        "breed": "Gotland",
        "sex": "ewe"
    }

    response = client.put("/sheep/1", json=updated_data)

    assert response.status_code == 200
    assert response.json() == updated_data

    get_response = client.get("/sheep/1")
    assert get_response.status_code == 200
    assert get_response.json() == updated_data