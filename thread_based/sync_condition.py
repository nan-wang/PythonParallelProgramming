from threading import Thread, Condition
import time

items = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items

        with condition:
            # condition.acquire()
            if not items:
                condition.wait()
                print('consumer notify: no tiem to consume')
            item = items.pop()
            print(f'consumer notify: consumed 1 item, {item}')
            print(f'consumer notify: items to consue are {len(items)}')
            condition.notify()
            # condition.release()

    def run(self):
        for i in range(20):
            time.sleep(3)
            self.consume()


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.counter = 0

    def produce(self):
        global condition
        global items

        with condition:
            if len(items) == 10:
                print(f'producer notify: items produced are {len(items)}')
                print(f'producer notify: stop producing')
                condition.wait()
            self.counter += 1
            items.append(self.counter)
            print(f'producer notify: produce {self.counter}, total items produced {len(items)}')
            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    prod = Producer()
    cons = Consumer()

    prod.start()
    cons.start()

    prod.join()
    cons.join()
