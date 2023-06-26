import logging
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

counter = 0

lock = threading.Lock()

def thread_lock(count):
    global counter
    threadname = threading.current_thread().name
    logger.info("Thread %s has started", threadname)
    for values in range(count):
        with lock:
            logger.info("Thread %s has acquired the lock 🔐", threadname)
            counter += 1
            time.sleep(2)
    logger.info("Thread %s has completed  ✅", threadname)
    return counter


def main():
    logger.info("Application has started")

    workers = 1
    with ThreadPoolExecutor(max_workers=workers) as execution:
        for turns in range(workers + 1):
            value = random.randrange(1, 3)
            execution.submit(thread_lock, value)

    logger.info("Counter: %d", counter)
    logger.info("Application has finished")


if __name__ == "__main__":
    main()
