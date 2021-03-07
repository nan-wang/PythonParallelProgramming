import multiprocessing
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)-10s %(message)s'
)


class MyProcess(multiprocessing.Process):
    def run(self) -> None:
        logging.info(f'called run method')
        return


if __name__ == '__main__':
    jobs = []
    for _ in range(5):
        p = MyProcess()
        jobs.append(p)

    for p in jobs:
        p.start()

    for p in jobs:
        p.join()
