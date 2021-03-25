from collections import deque
from sys import stdin
input = stdin.readline
n, m, k = map(int, input().split())

arr = [list(input()) for _ in range(n)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]


def bfs(i, j, k):
    q = deque()
    q.append((i, j, k))
    visited[i][j][k] = 1
    while q:
        x, y, skill = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][skill]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny][skill]:
                continue
            if arr[nx][ny] == '1' and skill > 0:
                visited[nx][ny][skill - 1] = visited[x][y][skill] + 1
                q.append((nx, ny, skill - 1))
            if arr[nx][ny] == '0':
                visited[nx][ny][skill] = visited[x][y][skill] + 1
                q.append((nx, ny, skill))
    return -1


ret = bfs(0, 0, k)
print(ret)