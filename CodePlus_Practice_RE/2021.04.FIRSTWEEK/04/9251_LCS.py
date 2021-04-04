arr1 = [0] + list(input())
arr2 = [0] + list(input())

dp = [[0] * len(arr1) for _ in range(len(arr2))]

for i in range(1, len(arr2)):
    char = arr2[i]
    for j in range(1, len(arr1)):
        if arr2[i] == arr1[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
mx = 0
for row in dp:
    mx = max(mx, max(row))
print(mx)