"""
Comparison of iterative method VS recursive solution of the classical Fibonacci sequence.

N is set to 35 for the experiment
"""
import time


def rec_fib(n):
    if n <= 1:
        return 1

    return rec_fib(n - 1) + rec_fib(n - 2)


def fib(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        n1 += n2
        n1, n2 = n2, n1

    return n2


N = 35

start_rec = time.perf_counter()
res_rec = rec_fib(N)
stop_rec = time.perf_counter()
delta_rec = stop_rec - start_rec

start_fib = time.perf_counter()
res = fib(N)
end_fib = time.perf_counter()
delta = end_fib - start_fib

print(f"Recursive Fibonacci of {N}\nResult: {res_rec}\ntime: {delta_rec}")
print()
print(f"Iterative Fibonacci of {N}\nResult: {res}\ntime: {delta}")
