from typing import List

import pytest
from pydantic import ValidationError

from python_topics.python_pydantic.main import User


def test_valid_user():
    user = User(name="John Smith", age=20, email="john.smith@example.com", password="Pa$$w0rd", roles=["admin"])
    assert user.name == "John Smith"
    assert user.age == 20
    assert user.email == "john.smith@example.com"
    assert user.password == "Pa$$w0rd"
    assert user.roles == ["admin"]


def test_invalid_user_age():
    with pytest.raises(ValidationError) as e:
        user = User(name="John Smith", age=17, email="john.smith@example.com", password="Pa$$w0rd", roles=["admin"])
    assert "Age must be 18 or older" in str(e.value)

def test_invalid_user_email():
    with pytest.raises(ValidationError) as e:
        user = User(name="John Smith", age=20, email="john.smith", password="Pa$$w0rd", roles=["admin"])
    assert "Invalid email format" in str(e.value)
