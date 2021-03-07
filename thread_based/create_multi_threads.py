import threading
import time


def foo_func():
    print(f'{threading.currentThread().getName()} is starting\n')
    time.sleep(2)
    print(f'{threading.currentThread().getName()} is existing\n')


if __name__ == '__main__':
    thread_list = [threading.Thread(name=f'func_{i}', target=foo_func) for i in range(3)]

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
