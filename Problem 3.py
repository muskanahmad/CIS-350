import random
import time


# Function to measure the execution time
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


# Recursive Algorithm
def rearrange_recursive(A, k):
    if not A:
        return []

    pivot = A[0]
    smaller = [x for x in A[1:] if x <= k]
    larger = [x for x in A[1:] if x > k]

    return rearrange_recursive(smaller, k) + [pivot] + rearrange_recursive(larger, k)


# Non-Recursive Method
def rearrange_non_recursive(A, k):
    smaller = [x for x in A if x <= k]
    larger = [x for x in A if x > k]
    return smaller + larger


# Example usage
array_size = 1000
A = [random.randint(1, 1000) for _ in range(array_size)]
k = random.randint(1, 1000)

result_recursive, time_recursive = measure_time(rearrange_recursive, A, k)
result_non_recursive, time_non_recursive = measure_time(rearrange_non_recursive, A, k)

print("Recursive Result:", result_recursive)
print("Recursive Execution Time:", time_recursive)

print("Non-Recursive Result:", result_non_recursive)
print("Non-Recursive Execution Time:", time_non_recursive)
