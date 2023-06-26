import pytest
from main import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_get(client):
    result = client.get("/notes")
    assert result.status_code == 200
