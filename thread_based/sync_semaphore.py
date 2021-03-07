import threading
import time
import random

semaphore = threading.Semaphore(0)

item = None


def consumer():
    global item
    print(f'consumer is waiting')
    semaphore.acquire()
    print(f'consumer notify: consumed item number {item}')


def producer():
    global item
    time.sleep(5)
    item = random.randint(0, 1000)
    print(f'producer notify: produced item number {item}')
    semaphore.release()


if __name__ == '__main__':
    for i in range(3):
        t_prod = threading.Thread(target=producer())
        t_cons = threading.Thread(target=consumer())
        t_prod.start()
        t_cons.start()
        t_prod.join()
        t_cons.join()

    print('main thread exiting')
