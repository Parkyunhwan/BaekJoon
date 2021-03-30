from collections import deque
from collections import defaultdict
import sys
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

shark = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            shark.append((i, j))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
visited = [[sys.maxsize] * m for _ in range(n)]

def bfs(sx, sy):
    global visited
    q = deque()
    q.append((sx, sy, 0))
    while q:
        x, y, count = q.popleft()

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] <= count + 1:
                continue
            if arr[nx][ny] == 1:
                continue
            visited[nx][ny] = count + 1
            q.append((nx, ny, count + 1))

result = 0

for i in range(len(shark)):
    bfs(shark[i][0], shark[i][1])


for i in range(n):
    for j in range(m):
        if visited[i][j] != sys.maxsize:
            result = max(result, visited[i][j])

print(result)