
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Calculator API is running!"


def test_add():
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtract():
    response = client.get("/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_multiply():
    response = client.get("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 50


def test_divide():
    response = client.get("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_divide_by_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"


def test_invalid_input():
    response = client.get("/add?a=hello&b=5")
    assert response.status_code == 422
