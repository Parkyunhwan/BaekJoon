dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def DFS(x, y):
    for k in range(4):
        tx, ty = x + dx[k], y + dy[k]
        if tx < 0 or tx >= n or ty < 0 or ty >= m or arr[tx][ty]:
            continue
        else:
            arr[tx][ty] = True
            DFS(tx, ty)


n, m = map(int, input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            DFS(i, j)
            count += 1
print(count)