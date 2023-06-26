import threading
import time


def using_main_thread(value_1, value_2, value_3, value_4) -> bool:

    try:

        def thread_1():
            time.sleep(5)
            print("Value by Thread-1:", value_1)

        def thread_2():
            print("Value by Thread-2:", value_2)

        def thread_3():
            time.sleep(4)
            print("Value by Thread-3:", value_3)

        def thread_4():
            time.sleep(1)
            print("Value by Thread-4:", value_4)

        # Creating sample threads
        thread1 = threading.Thread(target=thread_1)
        thread2 = threading.Thread(target=thread_2)
        thread3 = threading.Thread(target=thread_3)
        thread4 = threading.Thread(target=thread_4)

        print("Main thread for the given program:", threading.main_thread())

        # Starting the threads
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    except Exception as error:
        print("Exception in using_main_thread:", error)
        return False

    return True


def test_using_main_thread():
    using_main_thread(10, 20, 30, 50)


if __name__ == "__main__":
    test_using_main_thread()
