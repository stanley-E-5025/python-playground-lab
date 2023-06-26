import logging
import threading
import time

# Flag to indicate if the threads should stop
stop_flag = threading.Event()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(threadName)s: %(message)s")


def worker1():
    while not stop_flag.is_set():
        logging.info("I am a daemon thread running task 1")
        time.sleep(1)
    logging.info("Worker1 stopping")


def worker2():
    while not stop_flag.is_set():
        logging.info("I am a daemon thread running task 2")
        time.sleep(2)
    logging.info("Worker2 stopping")


def worker3():
    while not stop_flag.is_set():
        logging.info("I am a non-daemon thread running task 3")
        time.sleep(3)
    logging.info("Worker3 stopping")


def test():
    # Create and start daemon threads
    t1 = threading.Thread(target=worker1, name="worker-1")
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=worker2, name="worker-2")
    t2.daemon = True
    t2.start()

    # Create and start non-daemon thread
    t3 = threading.Thread(target=worker3, name="worker-3")
    t3.start()
    t3.join()
    logging.info("Exiting Main Thread")


if __name__ == "__main__":
    test()
    time.sleep(10)
    stop_flag.set()
