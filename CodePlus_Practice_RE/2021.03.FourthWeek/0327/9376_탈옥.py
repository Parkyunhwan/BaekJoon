import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, idx, h, w):
    global visited
    q = deque()
    q.append((x, y, 0))
    visited[x][y][idx] = 0
    while q:
        x, y, count = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= h + 2 or ny >= w + 2 or arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '#' and visited[nx][ny][idx] > count + 1:
                visited[nx][ny][idx] = count + 1
                q.append((nx, ny, count + 1))
            elif arr[nx][ny] != '#' and visited[nx][ny][idx] > count:
                visited[nx][ny][idx] = count
                q.append((nx, ny, count))

for _ in range(int(input())):
    h, w = map(int, input().split())
    visited = [[[sys.maxsize] * 3 for _ in range(w + 2)] for _ in range(h + 2)]
    arr = [['.'] * (w + 2)]
    for _ in range(h):
        tmp = ['.'] + list(input()) + ['.']
        arr.append(tmp)
    arr.append(['.'] * (w + 2))

    # 3개의 시작지점 지정 (0, 0), 죄수 2개
    start = [[0, 0]]
    for i in range(h + 2):
        for j in range(w + 2):
            if arr[i][j] == '$':
                start.append([i, j])

    for i, pos in enumerate(start):
        x, y = pos[0], pos[1]
        bfs(x, y, i, h, w)

    # 출력
    # for k in range(3):
    #     for i in range(h + 2):
    #         for j in range(w + 2):
    #             if visited[i][j][k] == sys.maxsize:
    #                 print('.', end=' ')
    #             else:
    #                 print(visited[i][j][k], end=' ')
    #         print()
    #     print()

    result = sys.maxsize
    for i in range(h + 2):
        for j in range(w + 2):
            total = 0
            for k in range(3):
                total += visited[i][j][k]

            if arr[i][j] == '#':
                total -= 2

            result = min(result, total)

    print(result)

