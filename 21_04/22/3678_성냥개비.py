# 성냥개비로 만들 수 있는 숫자의 최솟값을 저장한다.
# 0개 부터 8개 까지 최솟값
num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
min_dp = [0] * 101
for i in range(9):
    min_dp[i] = num[i]

# 한자릿수에서는 0이될수없으므로 예외 처리
min_dp[6] = 6

def min_calculate():
    for i in range(9, 101):
        min_dp[i] = min_dp[i - 2] * 10 + num[2]
        for j in range(3, 8):
            min_dp[i] = min(min_dp[i], min_dp[i - j] * 10 + num[j])

min_calculate()


for _ in range(int(input())):
    n = int(input())

    print(min_dp[n], end=' ')

    even = 0
    if n % 2 == 1:
        even = 7
        n -= 3

    while n != 0:
        even *= 10
        even += 1
        n -= 2

    print(even)