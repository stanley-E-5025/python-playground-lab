import pytest
from modules.create_jwt import CreateJWT

success = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHBpcmVkIjogMzYwMCwgImRhdGEiOiAidGVzdF9kYXRhIn0.YjhkNWJlYTYxODgwNTMwMmU3OTNhNTc2YTEyMzFjYWIyZWI5MTM4YjYwYTE4ZDA2OWUwYmE4MzMyMGNhZmM2Zg"
failure = False


@pytest.fixture(scope="function")
def create_jwt_success_instance():
    yield CreateJWT(expiration=3600, data="test_data", secret_key="key")


@pytest.fixture(scope="function")
def create_jwt_failure_instance():
    yield CreateJWT(expiration=3600, data=None, secret_key=None)


def test_create_jwt_success(create_jwt_success_instance):
    assert create_jwt_success_instance.create_token() == success


def test_create_jwt_failure(create_jwt_failure_instance):
    assert create_jwt_failure_instance.create_token() == failure
