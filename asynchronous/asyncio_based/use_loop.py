import asyncio
import logging

logging.basicConfig(
    format='%(asctime)s %(processName)-10s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def func_1(end_time, loop):
    logging.info(f'func_1 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_2, end_time, loop)
    else:
        loop.stop()


def func_2(end_time, loop):
    logging.info(f'func_2 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_3, end_time, loop)
    else:
        loop.stop()


def func_3(end_time, loop):
    logging.info(f'func_3 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_1, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

end_loop = loop.time() + 9.0
loop.call_soon(func_1, end_loop, loop)

loop.run_forever()
loop.close()