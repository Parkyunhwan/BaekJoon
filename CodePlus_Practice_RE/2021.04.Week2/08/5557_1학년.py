n = int(input())

arr = [0] + list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n + 1)]


dp[1][arr[1]] = 1
for i in range(1, n - 1):
    for j in range(0, 21):
        if dp[i][j] != 0:
            if j - arr[i + 1] >= 0:
                dp[i + 1][j - arr[i + 1]] += dp[i][j]
            if j + arr[i + 1] <= 20:
                dp[i + 1][j + arr[i + 1]] += dp[i][j]

# for row in dp:
#     print(row)
print(dp[n - 1][arr[n]])