n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

check = [[False] * m for _ in range(n)]
mx = 0


def dfs(x, y, sum_value, index):
    global mx
    if index == 4:
        mx = max(mx, sum_value)
        return
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not check[nx][ny]:
            check[nx][ny] = True
            dfs(nx, ny, sum_value + arr[nx][ny], index + 1)
            check[nx][ny] = False

def middle(x, y):
    result = 0
    if x >= 1 and y >= 1 and y < m - 1: # ㅗ
        result = max(result, arr[x - 1][y] + arr[x][y - 1] + arr[x][y] + arr[x][y + 1])
    if x >= 1 and x < n - 1 and y < m - 1:# ㅏ
        result = max(result, arr[x - 1][y] + arr[x + 1][y] + arr[x][y] + arr[x][y + 1])
    if x < n - 1 and y >= 1 and y < m - 1:
        result = max(result, arr[x + 1][y] + arr[x][y - 1] + arr[x][y] + arr[x][y + 1])
    if x >= 1 and x < n - 1 and y >= 1:
        result = max(result, arr[x - 1][y] + arr[x + 1][y] + arr[x][y] + arr[x][y - 1])
    return result


for i in range(n):
    for j in range(m):
        check[i][j] = True
        dfs(i, j, arr[i][j], 1)
        mx = max(mx, middle(i, j))
        check[i][j] = False
print(mx)