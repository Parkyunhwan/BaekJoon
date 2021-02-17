n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]

dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n]))

# n - 2에서 01, n - 1에서 0 한 것
# 1차원으로 구하는 방법 review
testcase = int(input())

dp = [0 for _ in range(91)]

for i in range(1, testcase + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[testcase])