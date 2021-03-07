import threading


def func(i):
    print(f'function called by thread {i}')
    return


threads = []
for i in range(5):
    t = threading.Thread(target=func, args=(i,))
    threads.append(t)
    t.start()
    t.join()