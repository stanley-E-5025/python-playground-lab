import logging
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def pool(item):
    s = random.randrange(1, 3)
    logging.info(f"Thread {item}: sleeping for {s} ⏱")
    time.sleep(s)
    logging.info(f"Thread {item}: Done ✅")
    return s

# Main function
def main():
    logging.info("Starting")

    workers = 5
    items = 10

    with ThreadPoolExecutor(max_workers=workers) as executor:
        result = list(executor.map(pool, range(items)))

    logging.info("Finishing")
    return result

if __name__ == "__main__":
    main()
