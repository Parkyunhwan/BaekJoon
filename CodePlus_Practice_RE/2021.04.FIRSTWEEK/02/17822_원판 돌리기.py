import sys
sys.setrecursionlimit(10000)
n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# d -> 0 시계, 1 반시
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False

def erase_num(x, y, val, visited):
    global flag
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        ny %= m
        if nx < 0 or nx >= n or visited[nx][ny]:
            continue
        if arr[nx][ny] == 0:
            continue
        if arr[nx][ny] == val:
            flag = True
            arr[nx][ny] = 0
            arr[x][y] = 0
            visited[nx][ny] = True
            erase_num(nx, ny, val, visited)

for f in range(t):
    x, d, k = map(int, input().split())
    mul = x
    x -= 1

    for i in range(x, n, mul):
        temp = []
        k %= m
        if d == 0:  # 시계 방향
            arr[i] = arr[i][-k:] + arr[i][:-k]
        elif d == 1:
            arr[i] = arr[i][k:] + arr[i][:k]

    visited = [[False] * m for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                val = arr[i][j]
                visited[i][j] = True
                erase_num(i, j, val, visited)
    avg = 0
    count = 0
    if not flag:
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:
                    count += 1
                    avg += arr[i][j]
        if count != 0:
            avg /= count
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == 0:
                        continue
                    if arr[i][j] < avg:
                        arr[i][j] += 1
                    elif arr[i][j] > avg:
                        arr[i][j] -= 1

sm = 0
for row in arr:
    sm += sum(row)
print(sm)