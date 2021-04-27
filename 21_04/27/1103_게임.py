'''
    해당문제를 bfs()로 방문 체크하면 한 경우에 대해 발생할 수 있는 경로를 모두 체크하지 못한다.

    따라서 dfs()를 사용해야한다.

    그냥 dfs()로 하면 똑같은 위치에서 찾는 경우가 중복 발생하므로 시간초과가 발생한다.
    이때 dp를 함께 써주면 효율성에서 이득을 볼 수 있다.
'''
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_count = 0
visited = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

circle = False

def dfs(x, y):
    global circle
    if x < 0 or y < 0 or x >= N or y >= M:
        return 0
    if arr[x][y] == 'H':
        return 0
    if visited[x][y]:
        #circle = True
        return -1
    if dp[x][y] != 0:
        return dp[x][y]
    visited[x][y] = True
    coin = int(arr[x][y])
    ret = 0
    for k in range(4):
        nx, ny = x + dx[k] * coin, y + dy[k] * coin
        val = dfs(nx, ny)
        if val == -1:
            ret = -1
            break
        ret = max(ret, val + 1)
    visited[x][y] = False
    dp[x][y] = ret
    return ret


val = dfs(0, 0)
if circle:
    print(-1)
else:
    print(val)

