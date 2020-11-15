# N, K = map(int, input().split())
# mod = 1000000000
# table = [1]
# table += [0] * N
# for _ in range(1, K+1):
#     for idx in range(1, N+1):
#         table[idx] = (table[idx] + table[idx-1])%mod
# print(table[N])

n, k = map(int, input().split())
mod = 1000000000
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(1, n+1):
    for j in range(n+1):
        for l in range(n+1): # 0의 경우도 포함해야한다.
            dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= mod

print(dp[k][n])
