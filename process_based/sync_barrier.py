import time
from datetime import datetime
import logging
from multiprocessing import Barrier, Lock, Process

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(processName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def func_with_barrier(synchronizer, serializer):
    time.sleep(2)
    synchronizer.wait()
    now = time.time()
    with serializer:
        logging.info(f'enter barrier -> {datetime.fromtimestamp(now)}')


def func_without_barrier():
    now = time.time()
    time.sleep(2)
    logging.info(f'enter without barrier -> {datetime.fromtimestamp(now)}')


if __name__ == '__main__':
    synchronizer = Barrier(5)
    serializer = Lock()
    p_barrier_list = []
    for i in range(5):
        p_barrier = Process(name=f'p{i}_with_barrier', target=func_with_barrier, args=(synchronizer, serializer))
        p_barrier_list.append(p_barrier)
    for p in p_barrier_list:
        p.start()

    p_no_barrier_list = []
    for i in range(5, 10):
        p_no_barrier = Process(name=f'p{i}_without_barrier', target=func_without_barrier)
        p_no_barrier_list.append(p_no_barrier)
    for p in p_no_barrier_list:
        p.start()
