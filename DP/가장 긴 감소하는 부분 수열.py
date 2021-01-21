n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
mx = 1

for i in range(len(arr)):
    dp[i] = 1
    for j in range(i):
        if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            mx = max(mx, dp[i])

print(mx)