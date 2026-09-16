from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# Successful POST test
def test_create_student():

    response = client.post(
        "/students",
        json={
            "id": 1,
            "name": "Rakib Hossain",
            "department": "CSE",
            "semester": 5,
            "cgpa": 3.80
        }
    )

    assert response.status_code == 200


# Successful GET test
def test_get_students():

    response = client.get("/students")

    assert response.status_code == 200


# Successful PUT test
def test_update_student():

    response = client.put(
        "/students/1",
        json={
            "id": 1,
            "name": "Rakib Updated",
            "department": "CSE",
            "semester": 6,
            "cgpa": 3.90
        }
    )

    assert response.status_code == 200


# Successful DELETE test
def test_delete_student():

    response = client.delete("/students/1")

    assert response.status_code == 200


# Invalid scenario 1
def test_get_invalid_student():

    response = client.get("/students/999")

    assert response.status_code == 404


# Invalid scenario 2
def test_create_duplicate_student():

    client.post(
        "/students",
        json={
            "id": 2,
            "name": "Test Student",
            "department": "EEE",
            "semester": 3,
            "cgpa": 3.50
        }
    )

    response = client.post(
        "/students",
        json={
            "id": 2,
            "name": "Another Student",
            "department": "CSE",
            "semester": 4,
            "cgpa": 3.70
        }
    )

    assert response.status_code == 400