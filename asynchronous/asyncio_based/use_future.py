import asyncio
import logging

logging.basicConfig(
    format='%(asctime)s %(processName)-10s %(funcName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S'
)

@asyncio.coroutine
def first_coroutine(future, N):
    count = 0
    for i in range(N):
        logging.info(f'calculate {i}')
        count += (i+1)
        yield from asyncio.sleep(1)
    future.set_result(f'first coroutine (sum(N)) result = {count}')


@asyncio.coroutine
def second_coroutine(future, N):
    count = 1
    for i in range(N):
        logging.info(f'calculate {i}')
        count *= (i+2)
        yield from asyncio.sleep(2)
    future.set_result(f'second coroutine (prod(N)) result = {count}')


def get_result(future):
    print(f'get result {future.result()}')


if __name__ == '__main__':
    N1 = 5
    N2 = 5

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future1.add_done_callback(get_result)
    future2 = asyncio.Future()
    future2.add_done_callback(get_result)

    tasks = [
        first_coroutine(future1, N1),
        second_coroutine(future2, N2),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()