import time
import multiprocessing


def factorize_worker(num):
    factors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    factors.sort()
    return factors


def factorize_serial(*numbers):
    start_time = time.perf_counter()  # Початок вимірювання часу
    result = []
    for num in numbers:
        factors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        factors.sort()
        result.append(factors)
    end_time = time.perf_counter()  # Завершення вимірювання часу
    elapsed_time = (end_time - start_time) * 1_000_000  # Перетворення часу до мікросекунд
    return result, elapsed_time


def factorize_parallel(*numbers):
    start_time = time.perf_counter()  # Початок вимірювання часу
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())  # Створення пулу процесів
    result = pool.map(factorize_worker, numbers)  # Розподіл завдань між процесами
    pool.close()  # Завершення пулу процесів
    pool.join()  # Очікування завершення всіх процесів
    end_time = time.perf_counter()  # Завершення вимірювання часу
    elapsed_time = (end_time - start_time) * 1_000_000  # Перетворення часу до мікросекунд
    return result, elapsed_time


if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)

    result_serial, elapsed_time_serial = factorize_serial(*numbers)
    result_parallel, elapsed_time_parallel = factorize_parallel(*numbers)

    print("Factorization of 128 (Serial):", result_serial[0])
    print("Factorization of 255 (Serial):", result_serial[1])
    print("Factorization of 99999 (Serial):", result_serial[2])
    print("Factorization of 10651060 (Serial):", result_serial[3])
    print("Elapsed time (Serial): {:.3f} microseconds".format(elapsed_time_serial))
    print()
    print("Factorization of 128 (Parallel):", result_parallel[0])
    print("Factorization of 255 (Parallel):", result_parallel[1])
    print("Factorization of 99999 (Parallel):", result_parallel[2])
    print("Factorization of 10651060 (Parallel):", result_parallel[3])
    print("Elapsed time (Parallel): {:.3f} microseconds".format(elapsed_time_parallel))
