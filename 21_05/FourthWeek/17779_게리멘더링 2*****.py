'''
    arr를 적용한 수정 필요...

    문제를 꼼꼼히 읽자...
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

mn = 1e9

def gary(x, y, d1, d2):
    global mn
    print(x, y, d1, d2)
    visited = [[0] * N for _ in range(N)]
    sx, sy = x, y
    x1, y1 = x, y
    x2, y2 = x + d2, y + d2
    visited[x1][y1] = 5
    visited[x2][y2] = 5

    for i in range(d1):
        x1, y1 = x1 - 1, y1 + 1
        x2, y2 = x2 - 1, y2 + 1
        visited[x1][y1] = 5
        visited[x2][y2] = 5

    for j in range(d2):
        x, y = x + 1, y + 1
        x1, y1 = x1 + 1, y1 + 1
        visited[x][y] = 5
        visited[x1][y1] = 5
    for v in visited:
        print(v)
    print()

    lx, ly = sx, sy
    ux, uy = sx - d1, sy + d1
    dx, dy = sx + d2, sy + d2
    rx, ry = dx - d1, dy + d1

    num = [0] * 6

    for i in range(0, ux):
        num[1] += (uy + 1)
        num[2] += (N - uy - 1)

    val = uy
    for i in range(ux, lx):
        num[1] += val
        val -= 1

    val = uy
    for i in range(ux, rx + 1):
        num[2] += (N - val - 1)
        val += 1

    val = ly
    for i in range(lx, dx + 1):
        num[3] += val
        val += 1

    val = ry - 1
    for i in range(rx + 1, dx + 1):
        num[4] += (N - val - 1)
        val -= 1

    for i in range(dx + 1, N):
        num[3] += dy
        num[4] += (N - dy)

    sm = sum(num)
    num[5] = N * N - sm
    num.sort()
    print(num, sum(num), num[5], num[1])
    if mn > num[5] - num[1]:
        mn = num[5] - num[1]





for i in range(N):
    for j in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if j + d1 + d2 < N and i - d1 >= 0 and i < i + d2 < N:
                    gary(i, j, d1, d2)

print(mn)