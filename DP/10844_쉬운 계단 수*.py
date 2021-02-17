# 규칙보단
# DP답게 푸는 방법을 생각해보자.
# 이전 인덱스를 -1, +1 값이 다음 인덱스로 들어가게 된다. 따라서, 이전 인덱스의 0~9까지를 기억해야한다.
# 0~9까지는 하나의 수가 아닌 여러 개의 수이므로 배열로 저장한다. -> 2차원 배열로 전체 단계 저장! DP

#REVIEW
n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]


for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
