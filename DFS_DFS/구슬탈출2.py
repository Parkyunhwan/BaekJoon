import sys
from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
blue = 0
red = 0
arr = []
check = [[[[False] * m for _ in range(n)] for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if arr[i][j] == 'B':
            blue = [i, j]
        elif arr[i][j] == 'R':
            red = [i, j]


def move(pos, i):
    x, y = pos[0], pos[1]
    _x, _y = dx[i], dy[i]
    count = 0
    while arr[x + _x][y + _y] != '#' and arr[x][y] != 'O':
        x += _x
        y += _y
        count += 1
    return x, y, count


check[blue[0]][blue[1]][red[0]][red[1]] = True
q = deque()
q.append((blue, red, 0))
while q:
    bl, re, n = q.popleft()
    if n >= 10:
        break
    for i in range(4):
        bx, by, bn = move(bl, i)
        rx, ry, rn = move(re, i)
        if arr[bx][by] == 'O':
            continue
        if arr[rx][ry] == 'O':
            print(n + 1)
            exit(0)
        if bx == rx and by == ry:
            if bn > rn:
                bx -= dx[i]
                by -= dy[i]
            else:
                rx -= dx[i]
                ry -= dy[i]
        if not check[rx][ry][bx][by]:
            check[rx][ry][bx][by] = True
            q.append(([bx, by], [rx, ry], n + 1))
print(-1)
