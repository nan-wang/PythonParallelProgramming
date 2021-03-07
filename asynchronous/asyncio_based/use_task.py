import asyncio
import logging

logging.basicConfig(
    format='%(asctime)s %(processName)-10s %(funcName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S'
)

@asyncio.coroutine
def factorial(x):
    f = 1
    for i in range(2, x+1):
        logging.info(f'x={i}')
        yield from asyncio.sleep(1)
        f *= i
    logging.info(f'factorial({x}) = {f}')

@asyncio.coroutine
def fibonacci(x):
    a, b = 0, 1
    for i in range(x):
        logging.info(f'x={i}')
        yield from asyncio.sleep(1)
        a, b = b, a + b
    logging.info(f'fibonacci({x}) = {a}, {b}')

@asyncio.coroutine
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
        logging.info(f'{i}')
        yield from asyncio.sleep(1)
    logging.info(f'binomial({n}, {k}) = {result}')


if __name__ == '__main__':
    tasks = [asyncio.Task(factorial(10)),
             asyncio.Task(fibonacci(10)),
             asyncio.Task(binomialCoeff(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
