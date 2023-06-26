import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_get(client):
    result = client.get("/")
    assert result.status_code == 200


def test_create(client):
    data = {
        "complexity": "test",
        "name": "Fermat factorization",
        "mathematical_ecuation": "n=x^2-y^2.  Then n=(x-y)(x+y) (1) and n is factored.",
        "description": "El método de factorización de Fermat se basa en la representación de un número natural impar como la diferencia de dos cuadrados",
    }
    result = client.post(
        "/create",
        data=data,
        headers={
            "Authorization": "Bearer eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHBpcmVkIjogMTY2NDU3NDc3OCwgInVzZXJuYW1lIjogInVzZXJuYW1lIiwgInBhc3N3b3JkIjogInBhc3N3b3JkIn0.Mjg1NTI1NDcwYWVjNjgxMTQzMGJjZDYwOTVkOGM1MjU5NWU1YjI1MDEyYjQ2M2ZmZmY3MmI0ZDAyNmZmODBjYw",
        },
    )

    assert data in result.data
    assert data in result.data.complexity == "test"
    assert data in result.data.name == "Fermat factorization"
    assert data in result.data.mathematical_ecuation == "n=x^2-y^2.  Then n=(x-y)(x+y) (1) and n is factored."


def test_update(client):
    result = client.patch(
        "/update/2",
        data={
            "complexity": "test",
            "name": "Fermat factorization",
            "mathematical_ecuation": "n=x^2-y^2.  Then n=(x-y)(x+y) (1) and n is factored.",
            "description": "El método de factorización de Fermat se basa en la representación de un número natural impar como la diferencia de dos cuadrados",
        },
        headers={
            "Authorization": "Bearer eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHBpcmVkIjogMTY2NDU3NDc3OCwgInVzZXJuYW1lIjogInVzZXJuYW1lIiwgInBhc3N3b3JkIjogInBhc3N3b3JkIn0.Mjg1NTI1NDcwYWVjNjgxMTQzMGJjZDYwOTVkOGM1MjU5NWU1YjI1MDEyYjQ2M2ZmZmY3MmI0ZDAyNmZmODBjYw",
        },
    )

    assert "UPDATE" in result.data


def test_delete(client):
    result = client.delete(
        "/delete/2",
        headers={
            "Authorization": "Bearer eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHBpcmVkIjogMTY2NDU3NDc3OCwgInVzZXJuYW1lIjogInVzZXJuYW1lIiwgInBhc3N3b3JkIjogInBhc3N3b3JkIn0.Mjg1NTI1NDcwYWVjNjgxMTQzMGJjZDYwOTVkOGM1MjU5NWU1YjI1MDEyYjQ2M2ZmZmY3MmI0ZDAyNmZmODBjYw",
        },
    )

    assert result.status_code == 200
    assert b"DELETE" in result.data
