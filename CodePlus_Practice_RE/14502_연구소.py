from collections import deque
import copy
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_count = 0


def spread_birus(back):
    q = deque()
    for i in range(n):
        for j in range(m):
            if back[i][j] == 2:
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if back[nx][ny] == 0:
                            back[nx][ny] = 2
                            q.append((nx, ny))
    return back

def count_safe(back):
    mx = 0
    for ar in back:
        for a in ar:
            if a == 0:
                mx += 1
    return mx


def makeWall(index):
    global max_count
    if index == 3:
        back = [a[:] for a in arr]
        back = spread_birus(back)
        if max_count < count_safe(back):
            max_count = max(max_count, count_safe(back))
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(index + 1)
                arr[i][j] = 0

makeWall(0)
print(max_count)