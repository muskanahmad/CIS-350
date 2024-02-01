def find_pair_recursive(A, k, start, end):
    while start < end:
        current_sum = A[start] + A[end]

        if current_sum == k:
            return A[start], A[end]
        elif current_sum < k:
            start += 1
        else:
            end -= 1

    return None


def find_pair_non_recursive(A, k):
    start, end = 0, len(A) - 1

    while start < end:
        current_sum = A[start] + A[end]

        if current_sum == k:
            return A[start], A[end]
        elif current_sum < k:
            start += 1
        else:
            end -= 1

    return None


import time
import random


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result


# Generate arrays
array_10 = sorted(random.sample(range(1, 100), 10))
array_100 = sorted(random.sample(range(1, 1000), 100))
array_1000 = sorted(random.sample(range(1, 10000), 1000))

# Measure and print times
for array in [array_10, array_100, array_1000]:
    print(f"Array size: {len(array)}")

    recursive_time, _ = measure_time(find_pair_recursive, array, 42, 0, len(array) - 1)
    print(f"Recursive Algorithm: {recursive_time} seconds")

    non_recursive_time, _ = measure_time(find_pair_non_recursive, array, 42)
    print(f"Non-Recursive Method: {non_recursive_time} seconds")

    print("\n")


