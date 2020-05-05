# from functools import lru_cache
#
#
# @lru_cache(maxsize=1000)


# Solution 1 -> Time: O(2^N), Space: O(N)
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


# Solution 2 -> Time: O(N), Space: O(N)
def fib2(num):
    cache = {0: 0, 1: 1}

    def memoize(n):
        if n in cache:
            return cache[n]
        cache[n] = memoize(n - 1) + memoize(n - 2)
        return memoize(n)

    return num if num <= 1 else memoize(num)


# Solution 3 -> Time: O(N), Space: O(1)
def fib3(n):
    if n <= 1: return n
    if n == 2: return 1
    current, prev1, prev2 = 0, 1, 1
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return current


def fib4(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n + 1) / 5 ** 0.5)


def time_test():
    def run(func):
        from time import time
        start = time()
        [func(_) for _ in range(30)]
        print(func.__name__, '\t', time() - start)
    [run(_) for _ in [fib, fib2, fib3, fib4]]


time_test()
