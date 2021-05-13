N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark = [[] for _ in range(M + 1)]
sharks_dir = [0] + list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            shark[arr[i][j]].append([i, j, sharks_dir[arr[i][j]]])
        arr[i][j] = None


dir_priority = [[[0] * 4 for _ in range(4)] for _ in range(M + 1)]
for i in range(1, M + 1):
    for j in range(4):
        dir_priority[i][j] = list(map(int, input().split()))

time = 0
while True:
    flag = True
    for i in range(1, M + 1):
        if shark[i] != [-1, -1, -1]:
            flag = False
            break
    if flag:
        break

    for index in range(1, M + 1):
        if arr[shark[index][0]][shark[index][1]] is None:
            arr[shark[index][0]][shark[index][1]] = [index, k]
        elif arr[shark[index][0]][shark[index][1]][0] == index:
            arr[shark[index][0]][shark[index][1]] = [index, k]
        else:
            shark = [-1, -1, -1]

    for i in range(1, M + 1):
        x, y, dir = shark[i]
        flag_blank = False
        for k in range(4):
            curr_dir = dir_priority[i][dir][k]
            nx, ny = x + dx[curr_dir], y + dy[curr_dir]
            if nx < 0 or ny < 0 or nx >= N or ny >= 0:
                continue
            if arr[nx][ny] is None:
                flag_blank = True
                shark[i] = [nx, ny, curr_dir]
                break
        flag_same = False
        if not flag_blank:
            for k in range(4):
                curr_dir = dir_priority[i][dir][k]
                nx, ny = x + dx[curr_dir], y + dy[curr_dir]
                if nx < 0 or ny < 0 or nx >= N or ny >= 0:
                    continue
                if arr[nx][ny] is None:
                    flag_same = True
                    shark[i] = [nx, ny, curr_dir]
                    break
        else:
            continue
        if not flag_same:
            shark[i] = [-1, -1, -1]

        for i in range(N):
            for j in range(N):
                if arr[i][j] is not None:
                    arr[i][j][1] -= 1
                    if arr[i][j][1] == 0:
                        arr[i][j] = None



