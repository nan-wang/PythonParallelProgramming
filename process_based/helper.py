import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)-10s %(message)s'
)


def FooFunc(i):
    logging.debug(f'called function in process: {i}')
    name = multiprocessing.current_process().name
    logging.debug(f'starting {name}')
    time.sleep(2)
    logging.debug(f'existing {name}')
    return