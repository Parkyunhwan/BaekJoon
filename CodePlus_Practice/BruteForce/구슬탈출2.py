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
