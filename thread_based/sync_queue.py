from threading import Thread
from queue import Queue
import time
import random
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s  %(message)s',
)


class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            self.queue.put(i)
            logging.debug(f'producer notify: item {i} appended to queue')
            time.sleep(1)


class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        while True:
            item = self.queue.get()
            logging.debug((f'consumer notify: item {item} poped from queue'))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    prod = Producer(queue)
    cons_list = [Consumer(queue) for _ in range(3)]
    prod.start()
    for c in cons_list:
        c.start()
    prod.join()
    for c in cons_list:
        c.join()


