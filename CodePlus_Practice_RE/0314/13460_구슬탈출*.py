# https://rebas.kr/725
# https://m.blog.naver.com/lizziechung/221859103444 (visited 검사의 새로운 방법 제시)
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def move_position(red, blue, direction):
    rx, ry, bx, by = red[0], red[1], blue[0], blue[1]

    # red, blue를 벽을 만나기 전까지 좌표로 보냄
    while arr[rx + dx[direction]][ry + dy[direction]] != '#' \
            and arr[rx][ry] != 'O':
        rx, ry = rx + dx[direction], ry + dy[direction]

    while arr[bx + dx[direction]][by + dy[direction]] != '#' \
            and arr[bx][by] != 'O':
        bx, by = bx + dx[direction], by + dy[direction]

    return rx, ry, bx, by


def find_hole(red, blue, count):
    global mn
    print(count)
    if count == 10:
        return
    print(red, blue)
    rx, ry, bx, by = red[0], red[1], blue[0], blue[1]
    for direction in range(4):  # left, right, up, down
        nrx, nry, nbx, nby = move_position(red, blue, direction)

        if visited[nrx][nry][nbx][nby]:
            continue

        red_diff_x, red_diff_y = abs(nrx - rx), abs(nry - ry),
        blue_diff_x, blue_diff_y = abs(nbx - bx), abs(nby - by)
        red_diff = red_diff_x + red_diff_y
        blue_diff = blue_diff_x + blue_diff_y

        if arr[nrx][nry] == 'O' and arr[nbx][nby] == 'O':
            continue
        elif arr[nrx][nry] == 'O' and arr[nbx][nby] != 'O':
            mn = min(mn, count + 1)
            continue
        elif arr[nrx][nry] != 'O' and arr[nbx][nby] == 'O':
            continue

        if nrx == nbx and nry == nby:
            if red_diff < blue_diff:
                nbx, nby = nbx - dx[direction], nby - dy[direction]
            else:
                nrx, nry = nrx - dx[direction], nry - dy[direction]

        visited[nrx][nry][nbx][nby] = True
        find_hole((nrx, nry), (nbx, nby), count + 1)

# 빨간, 파란공의 위치 파악
mn = 1e9
blue = []
red = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            blue.extend((i, j))
        elif arr[i][j] == 'R':
            red.extend((i, j))
visited[red[0]][red[1]][blue[0]][blue[1]] = True
find_hole(red, blue, 0)
print("ANSWER")
print(mn) if mn != 1e9 else print(-1)