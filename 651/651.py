def maxA2(N: int) -> int:

    def dp(n, a_num, copy):
        if n <= 0:
            return a_num
        
        A = dp(n - 1, a_num + 1, copy)  # A
        C_V = dp(n - 1, a_num + copy, copy)  # C-V
        C_A_C = dp(n - 2, a_num, a_num)  # C-A C-C
        return max(A, C_V, C_A_C)
    
    return dp(N, 0, 0)


def maxA(N: int) -> int:
    # 初始化容器, 用来存储个数的
    dp = [0] * (N+1)

    for i in range(1, N + 1):
        # 按A的个数, 就是前一个值 +1 次
        dp[i] = dp[i - 1] + 1
        for j in range(2, i):
            # 第三次才开始C-V
            if i <= j:
                continue
            # 得到C-V粘贴的个数; j 减 2 是给 C-A C-C 留下操作次数
            # 用乘法就是粘贴操作
            c_v_count = dp[j - 2] * (i - j + 1)
            # 然后用粘贴得到的个数和一直按A得到的个数比大小, 最大的也就是最多能有几个A, 覆盖掉按A得到的个数
            dp[i] = max(dp[i], c_v_count)

    return dp[N]


if __name__ == '__main__':
    print(maxA2(20))