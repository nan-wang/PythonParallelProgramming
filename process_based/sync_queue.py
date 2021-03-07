import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)-10s %(message)s')


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) -> None:
        for i in range(10):
            self.queue.put(i)
            logging.info(f'producer notify: item {i} appended to queue {self.name}')
            time.sleep(1)
            # skip for Mac OSX
            # logging.info(f'the size of queue: {self.queue.qsize()}')


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) -> None:
        while True:
            if self.queue.empty():
                logging.info(f'consumer notify: queue is empty')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                logging.info(f'consumer notify: item {item} popped from queue {self.name}')
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    prod = Producer(queue)
    cons = Consumer(queue)
    prod.start()
    cons.start()
    prod.join()
    cons.join()
