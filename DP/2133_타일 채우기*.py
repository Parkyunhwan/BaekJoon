# https://hjp845.tistory.com/28
n = int(input())

def sol(n):
    if n % 2 != 0:
        return 0
    else:
        dp = [0] * (n + 1)
        dp[0] = 1  # 0줄인 경우는 아무것도 안하는 경우 하나이니까
        dp[2] = 3
        for i in range(4, n + 1):
            dp[i] = dp[i - 2] * 3
            for j in range(i - 4, -1, -2):
                dp[i] += dp[j] * 2
        return dp[n]

print(sol(n))