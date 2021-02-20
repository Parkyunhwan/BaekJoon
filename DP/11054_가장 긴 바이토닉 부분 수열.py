n = int(input())

arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp2 = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = 1
    for j in range(i - 1, 0, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n, 0, -1):
    for j in range(i + 1, n + 1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(len(dp)):
    dp[i] = dp[i] + dp2[i]
print(max(dp))