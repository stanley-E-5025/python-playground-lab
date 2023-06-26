import time

import pytest
from daemon_thread.main import test


def test_workers():
    test()
    time.sleep(1)  # wait for the threads to start
    # assert that the logs contain the expected messages
    assert "I am a daemon thread running task 1" in caplog.text
    assert "I am a daemon thread running task 2" in caplog.text
    assert "I am a non-daemon thread running task 3" in caplog.text
    assert "Worker1 stopping" in caplog.text
    assert "Worker2 stopping" in caplog.text
    assert "Worker3 stopping" in caplog.text
    assert "Exiting Main Thread" in caplog.text
    assert "Exiting Main Thread" in caplog.text


@pytest.mark.usefixtures("caplog")
def test_stop_flag(caplog):
    test()
    time.sleep(11)
    assert "Worker1 stopping" in caplog.text
    assert "Worker2 stopping" in caplog.text
    assert "Worker3 stopping" in caplog.text
    assert "Exiting Main Thread" in caplog.text
