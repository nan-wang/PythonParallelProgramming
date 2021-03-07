import time
from threading import Thread, Event
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s)  %(message)s',)

items = []
event = Event()


class Consumer(Thread):
    def __init__(self, items, event):
        super(Consumer, self).__init__()
        self.items = items
        self.event = event

    def run(self) -> None:
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            logging.debug(f'consumer notify: {item} poped from list')
            self.event.clear()
        logging.debug(f'consumer notify: existing')


class Producer(Thread):
    def __init__(self, items, event):
        super(Producer, self).__init__()
        self.items = items
        self.event = event

    def run(self) -> None:
        for i in range(10):
            time.sleep(2)
            item = random.randint(0, 100)
            self.items.append(item)
            logging.debug(f'producer notify: item {item} appended to list')
            logging.debug(f'producer notify: event set')
            self.event.set()
            logging.debug(f'producer notify: event cleared')
        logging.debug(f'producer notify: existing')


if __name__ == '__main__':
    prod = Producer(items, event)
    cons = Consumer(items, event)
    prod.start()
    cons.start()
    prod.join()
    cons.join()
