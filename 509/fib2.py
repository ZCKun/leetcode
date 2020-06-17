import numpy as np


def fib(N):
    dp = np.zeros(N + 1, dtype=np.int)
    # base case
    dp[1] = dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


if __name__ == '__main__':
    print(fib(4))
