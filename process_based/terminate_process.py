import multiprocessing
import logging
from helper import FooFunc

if __name__ == '__main__':
    p = multiprocessing.Process(target=FooFunc(0))
    logging.info(f'before execution: {p.is_alive()}')
    p.start()
    logging.info(f'running: {p.is_alive()}')
    p.terminate()
    logging.info(f'terminated: {p.is_alive()}')
    p.join()
    logging.info(f'joined: {p.is_alive()}')
    logging.info(f'process exit code: {p.exitcode}')