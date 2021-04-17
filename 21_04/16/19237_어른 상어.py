'''
    https://velog.io/@koyo/boj-19237\
    https://yabmoons.tistory.com/496

'''
N, M, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

shark = [[0] * 3 for _ in range(N)]

blood = [[[0] * 2 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            shark[arr[i][j]] = [i, j, 0]
            blood[i][j] = [arr[i][j], k]

shark_dir_init = [0] + list(map(int, input().split()))
for i in range(1, len(shark_dir_init)):
    shark[i][2] = shark_dir_init[i]


priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(4)]

for row in priority:
    print(row)
print()

print(shark)

time = 0
while True:
    if time >= 1001:
        print(-1)
        exit(0)

    for i in range(1, N + 1):
        x, y, dir = shark[i]
        prior = priority[i][dir]
        flag = False
        for d in prior:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if blood[nx][ny][1] != 0:
                continue
            flag = True
            shark[i] = [nx, ny, d]
        if not flag:
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 2
            nx, ny = x + dx[dir], y + dy[dir]
            shark[i] = [nx, ny, dir]

    for i in range(N):
        for j in range(N):
            if blood[i][j][1] > 0:
                blood[i][j][1] -= 1
                if blood[i][j][1] == 0:
                    blood[i][j][0] = 0
    for i in range(1, len(shark)):
        x, y, dir = shark[i]
        if blood[x][y][0] <= i:
            blood[x][y] = [i, k]
