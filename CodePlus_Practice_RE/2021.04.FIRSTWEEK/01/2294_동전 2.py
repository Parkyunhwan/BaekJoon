n, k = map(int, input().split())

arr = [0] + list(int(input()) for _ in range(n))

dp = [1e9] * (k + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(arr[i], k + 1):
        #if arr[i] <= k:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[k] == 1e9:
    dp[k] = -1
print(dp[k])