import threading
import time

exit_flag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f'starting {self.name}')
        self.print_time()
        print(f'exiting {self.name}')

    def print_time(self):
        while self.counter:
            if exit_flag:
                self.exit()
            time.sleep(5)
            print(f'{self.name}: {time.ctime(time.time())}')
            self.counter -= 1


if __name__ == '__main__':
    thread1 = MyThread(1, 'thread-1', 1)
    thread2 = MyThread(2, 'thread-2', 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f'exiting the main process')
