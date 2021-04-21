n = int(input())

dp = [0] * (n + 1)
if n == 1:
    print(0)
    exit(0)
elif n <= 3:
    print(1)
    exit(0)

dp[1] = 0
dp[2] = 1
dp[3] = 1


for i in range(4, n + 1):
    a, b = n + 1, n + 1
    if i % 3 == 0:
        a = dp[i // 3] + 1
    if i % 2 == 0:
        b = dp[i // 2] + 1
    c = dp[i - 1] + 1
    dp[i] = min(a, b, c)

print(dp[n])