# 실패-- 손도 못
# 자릿수를 구분하는 것까진 이해함. 그 자릿수를 어떻게 이용할지
# -> 이차원 배열을 통해 이용
n = int(input())
d = [[0]*11 for _ in range(n+1)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % 1000000000

print(sum(d[n])%1000000000)