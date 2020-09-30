# https://regularmember.tistory.com/90
# velog
# 2차원 배열을 1차원 배열로 표현한 후 비트로 표현하는 법
# 비트마스크를 이용한 가로와 세로 구분
# 가로와 세로 & 행과 열의 관계
import sys

a, b = map(int, input().split())
ch = [[0] * b for i in range(a)]
arr = [list(map(int, sys.stdin.readline().strip())) for i in range(a)]
mx = -1
for val in range(1 << (a * b)):
    sm = 0
    seq = 0
    for i in range(a):
        seq = 0
        for j in range(b):
            k = i * b + j
            if val & (1 << k) != 0:
                seq = seq * 10 + arr[i][j]
            else:
                sm += seq
                seq = 0
        sm += seq

    seq = 0
    for j in range(b):
        seq = 0
        for i in range(a):
            # k = j * a + i ( 오답 )
            # k는 2차원 배열을 1차원으로 표현한 값이다.
            # 따라서 열 값에 행을 곱하고 행값을 더하는 것이 맞다.
            k = i * b + j
            if val & (1 << k) == 0:
                seq = seq * 10 + arr[i][j]
            else:
                sm += seq
                seq = 0
        sm += seq
    mx = max(mx, sm)
print(mx)

# bitmask

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
k = 0
mx = -1
while k < (1 << (n*m)):
    sm = 0
    # 가로 - 0
    for i in range(n):
        caro = 0
        for j in range(m):
            if (1 << i*m+j) & k == 0:
                caro = caro*10 + arr[i][j]
            else:
                sm += caro
                caro = 0
        sm += caro

    # 세로 - 1
    for j in range(m):
        sero = 0
        for i in range(n):
            if (1 << i*m+j) & k > 0:
                sero = sero*10 + arr[i][j]
            else:
                sm += sero
                sero = 0
        sm += sero

    mx = max(mx, sm)
    k += 1

print(mx)
