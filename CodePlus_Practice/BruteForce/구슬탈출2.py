#https://rebas.kr/725
import sys
import collections
n, m = map(int, sys.stdin.readline().split())
blue, red = (), ()
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
for i in range(1, n-1):
    for j in range(1, m-1):
        if arr[i][j] == ".":
            continue
        elif arr[i][j] == 'B':
            blue = (i, j)
        elif arr[i][j] == 'R':
            red = (i, j)

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)
q = collections.deque()
q.appendleft((blue, red, 0))
check[red[0]][red[1]][blue[0]][blue[1]] = True


def move(_v, _dx, _dy):
    _c = 0
    _x, _y = _v[0], _v[1]
    while arr[_x+_dx][_y+_dy] != '#' and arr[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c


def bfs():
    while q:
        b, r, d = q.pop()
        if d >= 10:
            break
        for i in range(4):
            nbx, nby, bc = move(b, dx[i], dy[i])
            nrx, nry, rc = move(r, dx[i], dy[i])
            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not check[nrx][nry][nbx][nby]:  # 레드, 블루가 완전히 똑같은 경우가 있었는지 확인하기 위해서
                check[nrx][nry][nbx][nby] = True
                q.appendleft(((nbx, nby), (nrx, nry), d+1))
    print(-1)
bfs()


# 3회차 코드

from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
red, blue = [], []
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_wall(rx, ry, bx, by, tx, ty):
    count_r = 0
    count_b = 0
    flag = False
    while arr[rx+tx][ry+ty] != '#':
        rx += tx
        ry += ty
        count_r += 1
        if arr[rx][ry] == 'O':
            flag = True
            break

    while arr[bx+tx][by+ty] != '#':
        bx += tx
        by += ty
        count_b += 1
        if arr[bx][by] == 'O':
            flag = True
            break

    if not flag and rx == bx and ry == by:
        if count_r > count_b:
            rx -= tx
            ry -= ty
        else:
            bx -= tx
            by -= ty

    return rx, ry, bx, by


def move(dir, rx, ry, bx, by):
    return check_wall(rx, ry, bx, by, dx[dir], dy[dir])


def BFS():
    q = deque()
    q.append((red, blue, 0))
    while q:
        r, b, count = q.popleft()
        if count >= 10:
            break
        rx, ry = r[0], r[1]
        bx, by = b[0], b[1]

        for i in range(4):
            nrx, nry, nbx, nby = move(i, rx, ry, bx, by)
            if arr[nbx][nby] == 'O':
                continue
            elif arr[nrx][nry] == 'O':
                return count + 1
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append(([nrx, nry], [nbx, nby], count + 1))
    return -1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            arr[i][j] = '.'
            red = [i, j]
        elif arr[i][j] == 'B':
            arr[i][j] = '.'
            blue = [i, j]
print(BFS())
