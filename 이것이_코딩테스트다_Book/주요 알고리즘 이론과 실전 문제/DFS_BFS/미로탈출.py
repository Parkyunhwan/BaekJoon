from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

q = deque()

q.append((0, 0))
while q:
    tx, ty = q.popleft()
    for dx, dy in (-1, 0),  (1, 0), (0, -1), (0, 1):
        nx, ny = tx + dx, ty + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or not arr[nx][ny]:
            continue
        if nx == n-1 and ny == m-1:
            print(arr[tx][ty]+1)
            exit(0)
        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[tx][ty] + 1
            q.append((nx, ny))



######################################
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

q = deque()

q.append((0, 0, 1))
while q:
    tx, ty, count = q.popleft()
    for dx, dy in (-1, 0),  (1, 0), (0, -1), (0, 1):
        nx, ny = tx + dx, ty + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or not arr[nx][ny]:
            continue
        if nx == n-1 and ny == m-1:
            print(count+1)
            exit(0)
        else:
            arr[nx][ny] = True
            q.append((nx, ny, count+1))

