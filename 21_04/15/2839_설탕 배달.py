n = int(input())

dp = [1e9] * (n + 1)

dp[0] = 0
dp[3] = 1
for i in range(5, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[n] >= 1e9:
    print(-1)
else:
    print(dp[n])