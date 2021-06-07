n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = min(dp[i - 3] + 1, dp[i - 1] + 1)

if dp[n] % 2:
    print("SK")
else:
    print("CY")