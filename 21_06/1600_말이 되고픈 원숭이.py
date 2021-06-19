import sys
from collections import deque

input = sys.stdin.readline
k = int(input())
W, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]

hdx = (-1, -2, -2, -1, +1, +2, +2, +1)
hdy = (-2, -1, +1, +2, -2, -1, +1, +2)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [[[0] * (k + 1) for _ in range(W)] for _ in range(H)]


def bfs(sx, sy, sk):
    q = deque()
    q.append((sx, sy, sk))

    while q:
        x, y, curr_k = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][curr_k]

        if curr_k > 0:  # 원숭이의 말의 이동 가능
            for t in range(8):
                nx, ny = x + hdx[t], y + hdy[t]

                if nx < 0 or ny < 0 or nx >= H or ny >= W or visited[nx][ny][curr_k - 1] != 0:
                    continue
                if arr[nx][ny] == 1:
                    continue
                visited[nx][ny][curr_k - 1] = visited[x][y][curr_k] + 1
                q.append((nx, ny, curr_k - 1))
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]

            if nx < 0 or ny < 0 or nx >= H or ny >= W or visited[nx][ny][curr_k] != 0:
                continue
            if arr[nx][ny] == 1:
                continue
            visited[nx][ny][curr_k] = visited[x][y][curr_k] + 1
            q.append((nx, ny, curr_k))
    return -1

print(bfs(0, 0, k))
