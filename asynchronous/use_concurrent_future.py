import concurrent.futures
import time

number_list = [i+1 for i in range(10)]


def count(number):
    for i in range(10000000):
        i += 1
    return i * number


def evaluate_item(x):
    result_item = count(x)
    # print(f'item {x}, result {result_item}')


if __name__ == '__main__':
    beg_time = time.process_time()
    for item in number_list:
        evaluate_item(item)
    print(f'sequential execution in {time.process_time() - beg_time} seconds')

    beg_time = time.process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print(f'Thread pool execution in {time.process_time() - beg_time} seconds')

    beg_time = time.process_time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print(f'Process pool execution in {time.process_time() - beg_time} seconds')


