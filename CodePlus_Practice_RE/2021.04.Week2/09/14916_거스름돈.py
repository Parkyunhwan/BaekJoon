n = int(input())

dp = [[1e9] * (n + 1) for _ in range(3)]

arr = [0, 2, 5]
dp[0][0] = 0
for i in range(1, len(arr)):
    dp[i][0] = 0
    for j in range(1, n + 1):
        if j >= arr[i]:
            dp[i][j] = min(dp[i][j], dp[i][j - arr[i]] + 1, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
mn = 1e9
for row in dp:
    mn = min(mn, row[n])
if mn == 1e9:
    print(-1)
else:
    print(mn)