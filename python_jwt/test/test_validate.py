import pytest
from modules.validate_jwt import ValidateJWT

token = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHBpcmVkIjogMzYwMCwgImRhdGEiOiAidGVzdF9kYXRhIn0.YjhkNWJlYTYxODgwNTMwMmU3OTNhNTc2YTEyMzFjYWIyZWI5MTM4YjYwYTE4ZDA2OWUwYmE4MzMyMGNhZmM2Zg"
success = True
failure = False


@pytest.fixture(scope="function")
def validate_jwt_success_instance():
    yield ValidateJWT(token=token, secret_key="key")


@pytest.fixture(scope="function")
def validate_jwt_failure_instance():
    yield ValidateJWT(token=token, secret_key=None)


def test_validate_jwt_success(validate_jwt_success_instance):
    assert validate_jwt_success_instance.validate_token() == success


def test_validate_jwt_failure(validate_jwt_failure_instance):
    assert validate_jwt_failure_instance.validate_token() == failure
