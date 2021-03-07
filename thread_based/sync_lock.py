import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


def increment_with_no_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_with_no_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


if __name__ == '__main__':
    func_list = [increment_with_lock, decrement_with_lock, increment_with_no_lock, decrement_with_no_lock]
    thread_list = [threading.Thread(target=func) for func in func_list]
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

    print(f'the value of shared variable with lock is {shared_resource_with_lock}')
    print(f'the value of shared variable with no lock is {shared_resource_with_no_lock}')
    """
    >> the value of shared variable with lock is 0
    >> the value of shared variable with no lock is -28318
    """
