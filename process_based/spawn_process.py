import multiprocessing

from helper import FooFunc

if __name__ == '__main__':
    job_list = []
    for i in range(5):
        p = multiprocessing.Process(
            target=FooFunc, args=(i,), name=f'foo_process_{i}')
        job_list.append(p)

    for p in job_list:
        p.start()

    for p in job_list:
        p.join()