from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
sm = 0
count = 0

flag = False


def dfs(i, j, visited, color):
    global sm, count, flag
    for k in range(4):

        ni, nj = i + dx[k], j + dy[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue
        if visited[ni][nj] != -1:
            continue
        if L <= abs(arr[ni][nj] - arr[i][j]) <= R:
            flag = True
            sm += arr[ni][nj]
            count += 1
            visited[ni][nj] = color
            dfs(ni, nj, visited, color)


def population_movement():
    global sm, count, flag
    visited = [[-1] * N for _ in range(N)]
    country = 0
    color = 0
    flag = False
    average = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                visited[i][j] = color
                sm = arr[i][j]
                count = 1
                dfs(i, j, visited, color)
                average[color] = sm // count
                color += 1
    if not flag:
        return False
    for i in range(N):
        for j in range(N):
            arr[i][j] = average[visited[i][j]]
    return True

move = 0
while True:
    if not population_movement():
        break
    move += 1
print(move)