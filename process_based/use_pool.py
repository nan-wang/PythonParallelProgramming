import multiprocessing
import logging

logging.basicConfig(
    format='%(asctime)s %(processName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def get_square(input):
    result = input*input
    logging.info(f'get input {input}, return output {result}')
    return result


if __name__ == '__main__':
    inputs = list(range(20))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(get_square, inputs)
    logging.info(f'mapping')
    pool.close()
    logging.info(f'closed')
    pool.join()
    logging.info(f'joined')
