import pytest
from main_thread.main import using_main_thread

success: bool = True
failure: bool = False


def test_using_main_thread():
    result = using_main_thread(10, 20, 30, 50)
    assert result == success
