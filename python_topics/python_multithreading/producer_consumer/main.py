import logging
import multiprocessing
import random
from queue import Queue


def create_work(queue, max):
    """Producer function"""
    logging.info("Producer process started")
    for items in range(max):
        value = random.randint(1, 100)
        queue.put(value)
        logging.info(f"Producing {items}: {value}")
    logging.info("Producer process finished")
    return queue

def perform_work(queue):
    """Consumer function"""
    logging.info("Consumer process started")
    consumed = []
    counter = 0
    while not queue.empty():
        value = queue.get()
        consumed.append(value)
        logging.info(f"Consuming {counter}: {value}")
        counter += 1
    logging.info("Consumer process finished")
    return consumed

def main():
    logging.basicConfig(level=logging.INFO)
    max = 10
    queue = multiprocessing.Queue()
    finished = multiprocessing.Queue()

    producer = multiprocessing.Process(target=create_work, args=[queue, finished, max])
    consumer = multiprocessing.Process(target=perform_work, args=[queue, finished])

    producer.start()
    consumer.start()

    producer.join()
    logging.info("Producer has finished")

    consumer.join()
    logging.info("Consumer has finished")

    logging.info("Finished")

if __name__ == "__main__":
    main()
