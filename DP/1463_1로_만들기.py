# 210216 풀이
import sys
n = int(input())

check = [sys.maxsize] * (n + 1)
i = 1
check[i] = 0
while i <= n:
    if i * 2 <= n and check[i * 2] > check[i] + 1:
        check[i * 2] = check[i] + 1
    if i * 3 <= n and check[i * 3] > check[i] + 1:
        check[i * 3] = check[i] + 1
    if i + 1 <= n and check[i + 1] > check[i] + 1:
        check[i + 1] = check[i] + 1
    i += 1

print(check[n])

# 내가 이전에 풀엇던 풀이
n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
dp[1] = 0
for i in range(1, n+1):
    for k in (i+1), (i*2), (i*3):
        if k <= n:
            dp[k] = min(dp[i] + 1, dp[k])

print(dp[n])
