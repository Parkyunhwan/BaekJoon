# 맞왜틀..?
n = int(input())

arr = []
visited = [[-1] * n for _ in range(n)]
count = 0
dx = [-1, -1, 1, 1, 0, 0]
dy = [0, 1, 0, -1, 1, -1]

for _ in range(n):
    arr.append(list(input()))


def dfs(x, y, c):

    check_num = []
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] == 'X' and visited[nx][ny] >= 0:
            check_num.append(visited[nx][ny])

    check_num = list(set(check_num))
    check_num.sort()
    curr = -1
    for i, val in enumerate(check_num):
        if i != val:
            curr = i
            break
    if curr == -1:
        curr = len(check_num)
    visited[x][y] = curr
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] == -1 and arr[nx][ny] == 'X':
            dfs(nx, ny, c + 1)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X' and visited[i][j] == -1:
            dfs(i, j, count)

check_num = [False] * 2500
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] >= 0 and not check_num[visited[i][j]]:
            check_num[visited[i][j]] = True
            count += 1

print(count)