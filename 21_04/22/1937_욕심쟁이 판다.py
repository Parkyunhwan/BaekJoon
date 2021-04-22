'''
    처음에 dfs와 dp를 결합해서 푸는 것이라 느꼈지만

    시도가 어려웠던 이유는

    이전에 들어왔던 길에 따라 dfs 값이 달라질 것이란 착각 때문이였다.
    하지만, dfs는 이전보다 큰값에만 진입할 수 있으므로 dfs가 달라지는 경우는 발생하지 않는다.

    따라서, dfs와 dp를 결합해서 문제를 해결하면 된다.
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

# 큰수로만 뻗어 나갈 뿐 작은수로 뻗어나갈수는 없다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    ret = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[x][y] < arr[nx][ny]:
            ret = max(ret, dfs(nx, ny))

    dp[x][y] = ret + 1
    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i, j)
mx = 0
for row in dp:
    mx = max(max(row), mx)

print(mx)








