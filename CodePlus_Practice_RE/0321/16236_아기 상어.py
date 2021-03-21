from collections import deque

n = int(input())
arr = []


baby_shark = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        j = tmp.index(9)
        baby_shark = [i, j]
    arr.append(tmp)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solve():
    x, y, size = baby_shark[0], baby_shark[1], 2
    time = 0
    cnt = 0
    while True:
        fishes = []
        if find_fishes(fishes, x, y, size) == -1:
            break
        else:
            size, cnt, time, x, y = eat_fish(fishes, x, y, time, size, cnt)
            print(size, cnt, time, x, y)


    print(time)


def eat_fish(fishes, sx, sy, time, size, cnt):
    print(fishes)
    fishes = sorted(fishes, key=lambda x: (x[1], x[0]))
    cx, cy, dist = fishes[0]
    tmp = arr[sx][sy]
    arr[sx][sy] = 0
    arr[cx][cy] = tmp
    time += dist
    cnt += 1
    if size == cnt:
        size += 1
        cnt = 0
    return size, cnt, time, cx, cy


def find_fishes(fishes, x, y, size):
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    shark_size = size
    found = -1
    visited[x][y] = True
    while q:
        x, y, dist = q.popleft()

        if dist == found:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if shark_size < arr[nx][ny]:
                continue
            visited[nx][ny] = True
            if 0 < arr[nx][ny] < shark_size:
                found = dist + 1
                fishes.append((nx, ny, dist + 1))
            q.append((nx, ny, dist + 1))
    return found






solve()


