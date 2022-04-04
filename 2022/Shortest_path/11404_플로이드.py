import sys
n = int(input())
m = int(input())
INF = sys.maxsize

d = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    d[a - 1][b - 1] = min(d[a - 1][b - 1], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i][j] = 0
            elif d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for d_com in d:
    for dd_com in d_com:
        if dd_com == INF:
            print(0, end=' ')
        else:
            print(dd_com, end=' ')
    print()