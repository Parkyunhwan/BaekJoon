from itertools import permutations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(robot_pos):
    x, y = robot_pos
    q = deque()
    q.append((x, y))
    visited = [[-1] * w for _ in range(h)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny] != -1:
                continue
            if arr[nx][ny] == 'x':
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(input()) for _ in range(h)]

    robot = []
    trash = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                robot = [i, j]
            elif arr[i][j] == '*':
                trash.append((i, j))
    trash_perm = []
    for i in range(1, len(trash) + 1):
        trash_perm.append(i)

    trash_perm = list(permutations(trash_perm, len(trash)))

    dv = [bfs(robot)]

    flag = False
    for i in range(len(trash)):
        if dv[0][trash[i][0]][trash[i][1]] == -1:
            result.append(-1)
            flag = True
            break
        dv.append(bfs(trash[i]))
    if flag:
        continue
    mn = 500
    for perm in trash_perm:
        sm = 0
        prev = 0
        for val in perm:
            x, y = trash[val - 1]
            sm += dv[prev][x][y]
            prev = val
        mn = min(mn, sm)
    result.append(mn)

for val in result:
    print(val)
