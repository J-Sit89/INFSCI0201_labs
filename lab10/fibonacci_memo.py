import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def recur_fibo_memoized(n):
    if n <= 1:
        return n
    else:
        return recur_fibo_memoized(n - 1) + recur_fibo_memoized(n - 2)

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

if __name__ == "__main__":
    n = 35
    
    start = time.time()
    print(f"Fibonacci({n}) without memoization: {recur_fibo(n)}")
    print(f"Time taken (no memoization): {time.time() - start:.4f} seconds")

    start = time.time()
    print(f"Fibonacci({n}) with memoization: {recur_fibo_memoized(n)}")
    print(f"Time taken (with memoization): {time.time() - start:.4f} seconds")
