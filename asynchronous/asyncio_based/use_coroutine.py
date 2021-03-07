import asyncio
import time
from random import randint

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(processName)-8s %(funcName)-10s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


@asyncio.coroutine
def StartState():
    logging.info(f'startState')
    input_value = randint(0, 1)
    time.sleep(1)
    next_state_func = State2 if input_value == 0 else State1
    result = yield from next_state_func(input_value)
    logging.info(f'resume the transition, calling {result}')


@asyncio.coroutine
def State1(transition_value):
    output_str = f'state1 with {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    next_state_func = State3 if input_value == 0 else State2
    result = yield from next_state_func(input_value)
    result = f'state1 with transition to {result}'
    logging.info(f'resume the transition, calling {result}')
    return output_str + result

@asyncio.coroutine
def State2(transition_value):
    output_str = f'state2 with {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    next_state_func = State1 if input_value == 0 else State3
    result = yield from next_state_func(input_value)
    result = f'state2 with transition to {result}'
    logging.info(f'resume the transition, calling {result}')
    return output_str + result

@asyncio.coroutine
def State3(transition_value):
    output_str = f'state3 with {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    next_state_func = State1 if input_value == 0 else EndState
    result = yield from next_state_func(input_value)
    result = f'state3 with transition to {result}'
    logging.info(f'resume the transition, calling {result}')
    return output_str + result

@asyncio.coroutine
def EndState(transition_value):
    output_str = f'end state with {transition_value}\n'
    logging.info('...stop computation')
    return output_str


if __name__ == '__main__':
    logging.info('start computation')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())
