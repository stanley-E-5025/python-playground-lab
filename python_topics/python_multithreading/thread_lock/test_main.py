import pytest
from thread_lock.main import thread_lock


@pytest.mark.parametrize("count", [1])
def test_thread_lock(count):
    global counter
    counter = 0
    result = thread_lock(count)
    assert result == count