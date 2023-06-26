import pytest
from thread_pool.main import pool


def test_pool():
    s = pool(1)
    assert isinstance(s, int)
    assert 0 < s < 3