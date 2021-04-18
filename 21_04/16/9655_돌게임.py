'''
    https://www.acmicpc.net/workbook/view/81
    코딩테스트 기출 (돌게임)
'''
# N = int(input())
# if N % 2 == 0:
#     print("CY")
# else:
#     print("SK")

# 최소한의 게임

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = min(dp[i - 3] + 1, dp[i - 1] + 1)

if dp[n] % 2:
    print("SK")
else:
    print("CY")
