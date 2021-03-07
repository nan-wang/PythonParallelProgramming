import multiprocessing
import logging

logging.basicConfig(
    format='%(asctime)s %(processName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H-%M-%S')


def worker(dictionary, key, value):
    logging.info(f'add {key}:{value}')
    dictionary[key] = value


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [multiprocessing.Process(
        target=worker,
        args=(dictionary, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    logging.info(f'main process exit: {dictionary}')
