import numpy as np


def fib(N) -> int:
    if N < 1:
        return N
    memo = np.zeros(N + 1, dtype=np.int)
    return helper(memo, N)


def helper(memo, n) -> int:
    # base case
    if n == 1 or n == 2:
        return 1

    if memo[n] != 0:
        return memo[n]

    memo[n] = helper(memo, n-1) + helper(memo, n-2)
    return memo[n]


if __name__ == '__main__':
    print(fib(4))
