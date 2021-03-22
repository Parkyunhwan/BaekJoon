from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(n)]

min_value = 1e9


def bfs():
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]

    q = deque()
    visited[1][0][0] = 1
    q.append((0, 0, 0, 1))

    while q:
        x, y, count, skill = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[skill][x][y]

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 1 and skill:
                visited[0][nx][ny] = visited[1][x][y] + 1
                q.append((nx, ny, count + 1, 0))
            elif arr[nx][ny] == 0 and not visited[skill][nx][ny]:
                visited[skill][nx][ny] = visited[skill][x][y] + 1
                q.append((nx, ny, count + 1, skill))
    return -1


val = bfs()

print(val)
