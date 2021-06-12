N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

result = 1e9
flower = []


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def calc():
    sm = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                sm += arr[i][j]

    return sm

def dfs(index):
    global result
    if index == 3:
        result = min(result, calc())
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            flag = True
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if visited[nx][ny]:
                    flag = False
                    break
            if not flag:
                continue

            visited[i][j] = True
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                visited[nx][ny] = True

            dfs(index + 1)

            visited[i][j] = False
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                visited[nx][ny] = False

dfs(0)

print(result)