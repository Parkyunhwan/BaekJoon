dp = [0] * 5001
dp[0] = 1

L = []
for _ in range(int(input())):
    L.append(int(input()))

for i in range(2, max(L) + 1):
    for j in range(2, i + 1):
        dp[i] += (dp[i - j] * dp[j - 2])
        dp[i] %= 1000000007

for l in L:
    print(dp[l])