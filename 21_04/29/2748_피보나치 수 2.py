N = int(input())

dp = [-1] * (N + 1)

def fibo(n):
    if dp[n] != -1:
        return dp[n]
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

def fibo_iter(n):
    if n <= 2:
        return 1
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibo_iter(N))