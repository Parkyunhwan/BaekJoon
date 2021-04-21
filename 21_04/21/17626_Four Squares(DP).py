n = int(input())
dp = [1e9] * (n + 1)

dp[1] = 1

val = 1
for i in range(1, n + 1):
    if pow(val + 1, 2) == i:
        val += 1
        dp[i] = 1
    else:
        for j in range(val, 0, -1):
            dp[i] = min(dp[i], dp[pow(j, 2)] + dp[i - pow(j, 2)])

print(dp[n])