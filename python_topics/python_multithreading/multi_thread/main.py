import logging
import threading
import time


def download_worker(id, url):
    """Thread worker function to download file"""
    logging.info(f"Worker {id} thread started")
    filename = url.split("/")[-1]
    time.sleep(2) # simulate download time
    logging.info(f"Worker {id} thread finished downloading {filename}")
    return filename


def main():
    """Main thread function"""
    logging.basicConfig(level=logging.INFO)
    logging.info("Main thread started")

    # List of files to download
    urls = [
        "http://www.example.com/file1.zip",
        "http://www.example.com/file2.zip",
        "http://www.example.com/file3.zip",
        "http://www.example.com/file4.zip",
        "http://www.example.com/file5.zip"
    ]

    # Create and start download worker threads
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_worker, args=(i, url))
        threads.append(t)
        t.start()

    # Do some work in the main thread
    logging.info("Main thread working")

    # Wait for all worker threads to finish
    for t in threads:
        t.join()
    logging.info("Main thread finished")

if __name__ == "__main__":
    main()
