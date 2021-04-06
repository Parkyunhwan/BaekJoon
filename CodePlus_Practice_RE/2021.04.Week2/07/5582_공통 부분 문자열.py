arr1 = [0] + list(input())
arr2 = [0] + list(input())

dp = [[0] * (len(arr2)) for _ in range(len(arr1))]


for i in range(1, len(arr1)):
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = 0
mx = 0
for row in dp:
    mx = max(max(row), mx)

print(mx)