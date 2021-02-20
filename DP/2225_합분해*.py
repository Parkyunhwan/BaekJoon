# 검색을 통해 다시 이해해보기..
n, k = map(int, input().split())

dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        for t in range(i + 1):
            dp[i][j] += dp[i - t][j - 1]
            dp[i][j] %= 1000000000
print(sum(dp[n]) % 1000000000)