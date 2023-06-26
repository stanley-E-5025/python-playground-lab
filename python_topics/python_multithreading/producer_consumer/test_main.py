import multiprocessing
from queue import Queue

from producer_consumer.main import create_work, perform_work


def test_create_work():
    q = multiprocessing.Queue()
    max = 10
    create_work(q, max)
    # Count the number of items in the queue
    count = 0
    while not q.empty():
        q.get()
        count += 1
    assert count == max

def test_perform_work():
    q = multiprocessing.Queue()
    for i in range(10):
        q.put(i)
    result = perform_work(q)
    assert result == list(range(10))