# 틀림 -> 왜틀림?

t = int(input())

for _ in range(t):
    n = int(input())
    d = [[0]*(n+1) for _ in range(3)]
    arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(2)]
    d[1][0] = arr[1][0]; d[1][1] = arr[1][1]
    for i in range(2, n+1):
        d[1][i] = max(d[2][i-1], d[2][i-2]) + arr[1][i]
        d[2][i] = max(d[1][i-1], d[1][i-2]) + arr[2][i]

    print(max(d[1][n], d[2][n]))
