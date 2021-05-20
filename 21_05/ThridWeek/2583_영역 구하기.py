import sys
sys.setrecursionlimit(100000)
M, N, K = map(int, input().split())

arr = [[False] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = True

def dfs(x, y):
    global count
    arr[x][y] = True
    count += 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= M or ny >= N or arr[nx][ny]:
            continue
        dfs(nx, ny)

ret = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            count = 0
            dfs(i, j)
            ret.append(count)

ret.sort()
print(len(ret))
for val in ret:
    print(val, end=' ')

