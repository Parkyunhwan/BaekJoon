n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dongjun = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            dongjun.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mn = 1e9


def dfs(dongjun, count):
    global mn
    x1, y1 = dongjun[0][0], dongjun[0][1]
    x2, y2 = dongjun[1][0], dongjun[1][1]

    if count == 10:
        return

    for k in range(4):
        nx1, ny1 = x1 + dx[k], y1 + dy[k]
        nx2, ny2 = x2 + dx[k], y2 + dy[k]
        ret1 = False
        ret2 = False
        if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m:
            ret1 = True
        if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m:
            ret2 = True
        if (ret1 and not ret2) or (not ret1 and ret2):
            mn = min(mn, count + 1)
            continue
        if ret1 and ret2:
            continue

        if arr[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if arr[nx2][ny2] == '#':
            nx2, ny2 = x2, y2

        if not check[nx1][ny1][nx2][ny2]:
            check[nx1][ny1][nx2][ny2] = True
            tmp = [(nx1, ny1), (nx2, ny2)]
            dfs(tmp, count + 1)
            check[nx1][ny1][nx2][ny2] = False


check[dongjun[0][0]][dongjun[0][1]][dongjun[1][0]][dongjun[1][1]] = True
dfs(dongjun, 0)

if mn == 1e9:
    print(-1)
else:
    print(mn)
