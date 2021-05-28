'''
    시계 방향, 반시계 방향으로 이동 시 방향 조심

    문제의 조건을 꼼꼼히 읽기

'''

import sys
sys.setrecursionlimit(10000)
N, M, T = map(int, input().split())

# 1부터 시작하도록 설정
arr = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sum_value = 0


def dfs(visited, x, y, same):
    global arr, change_flag
    visited[x][y] = True

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        ny %= M
        if nx < 0 or nx >= N or visited[nx][ny]:
            continue
        if arr[nx][ny] == 0:
            continue
        if same == arr[nx][ny]:
            change_flag = True
            arr[nx][ny] = 0
            arr[x][y] = 0
            dfs(visited, nx, ny, same)

for _ in range(T):
    x, d, k = map(int, input().split())

    for idx in range(x, N + 1, x):
        i = idx - 1
        k %= M # 중요...
        if d == 0:  # 시계
            arr[i] = arr[i][-k:] + arr[i][:-k]
        else:
            arr[i] = arr[i][k:] + arr[i][:k]



    # 인접한 모든 좌표 검사
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    change_flag = False
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] != 0:
                dfs(visited, i, j, arr[i][j])

    sum_value = 0
    count = 0
    if change_flag:
        continue
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                sum_value += arr[i][j]
                count += 1
    if count > 0:
        avg = sum_value / count
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    if arr[i][j] > avg:
                        arr[i][j] = arr[i][j] - 1
                    elif arr[i][j] < avg:
                        arr[i][j] = arr[i][j] + 1

sm = 0
for a in arr:
    sm += sum(a)
print(sm)