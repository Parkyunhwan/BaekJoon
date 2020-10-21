n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
dp[1] = 0
for i in range(1, n+1):
    for k in (i+1), (i*2), (i*3):
        if k <= n:
            dp[k] = min(dp[i] + 1, dp[k])

print(dp[n])