from collections import deque
n = int(input())

arr = [list(input()) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(arr, setting):  # 정상
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = arr[i][j]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if not setting:
                            if not visited[nx][ny] and arr[nx][ny] == color:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                        else:
                            if not visited[nx][ny] and \
                                    color != 'B' and \
                                    (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
                                visited[nx][ny] = True
                                q.append((nx, ny))
                            elif not visited[nx][ny] and \
                                    color == 'B' and \
                                    (arr[nx][ny] == color):
                                visited[nx][ny] = True
                                q.append((nx, ny))
                count += 1
    return count


def bfs2():
    exit(0)

print(bfs(arr, False), bfs(arr, True))

