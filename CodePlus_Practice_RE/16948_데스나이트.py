from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1,1]
dist = [[0] * n for _ in range(n)]

q = deque()
q.append((r1, c1))

while q:
    r, c = q.popleft()
    if r == r2 and c == c2:
        print(dist[r][c])
        exit(0)
    for k in range(6):
        nr, nc = r + dx[k], c + dy[k]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if dist[nr][nc] == 0:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

print(-1)

