import multiprocessing
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(processName)-10s %(message)s'
)


def create_items(pipe):
    output_p, _ = pipe
    for i in range(10):
        output_p.send(i)
        logging.info(f'send item {i}')
    output_p.close()
    logging.info(f'close pipe')


def multiply_items(pipe_read, pipe_write):
    close, input_p = pipe_read
    close.close()
    output_p, _ = pipe_write
    try:
        while True:
            item = input_p.recv()
            output_p.send(item * item)
            logging.info(f'send item {item * item}')
    except EOFError:
        output_p.close()
        logging.info(f'close pipe')


if __name__ == '__main__':
    p_read = multiprocessing.Pipe(True)
    proc_p_read = multiprocessing.Process(
        target=create_items, args=(p_read,)
    )
    proc_p_read.start()

    p_write = multiprocessing.Pipe(True)
    proc_p_write = multiprocessing.Process(
        target=multiply_items, args=(p_read, p_write,)
    )
    proc_p_write.start()

    p_read[0].close()
    p_write[0].close()

    try:
        while True:
            logging.info(f'p_write receive: {p_write[1].recv()}')
    except EOFError:
        logging.info(f'main process exited')