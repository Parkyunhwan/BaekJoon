'''
    냄새를 너무 빨리 update해서 틀림.

'''

from collections import deque
import copy
N, M, k = map(int, input().split())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

arr = [list(map(int, input().split())) for _ in range(N)]
shark = [[0, 0, 0] for _ in range(M + 1)]

shark_dir = [0] + list(map(int, input().split()))

prior = [[[0] * 4 for _ in range(4)] for _ in range(M)]
for i in range(M): # 상어 번호
    for dir in range(4): # 위 아래 왼 오
        prior[i][dir] = list(map(int, input().split()))

visited = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # 상어 번호, 냄새

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            shark[arr[i][j]] = [i, j, shark_dir[arr[i][j]]]
            visited[i][j] = [arr[i][j], k, False]


count = 0
while True:
    if count == 1001:
        print(-1)
        exit(0)

    for idx in range(1, len(shark)):
        curr_shark = shark[idx]
        x, y, dir = curr_shark
        if x == -1:
            continue
        shark_num, curr_remain, my_smell = visited[x][y]

        flag = True
        for d in prior[shark_num - 1][dir - 1]:
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            s_num, remain, next_smell = visited[nx][ny]
            if curr_remain + 1 == remain and shark_num > s_num and not next_smell:
                shark[idx] = [-1, -1, -1]
                flag = False
                break
            if remain == 0 or count >= remain:
                shark[idx] = [nx, ny, d]
                visited[nx][ny] = [shark_num, curr_remain + 1, False]
                flag = False
                break

        # 자기 자신의 구역으로 이동
        flag_same = False
        if flag:
            for d in prior[shark_num - 1][dir - 1]:
                nx, ny = x + dx[d], y + dy[d]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if visited[nx][ny][0] == shark_num:
                    flag_same = True
                    shark[idx] = [nx, ny, d]
                    visited[nx][ny] = [shark_num, curr_remain + 1, True]
                    break
        else:
            continue
        if not flag_same:
            shark[idx] = [-1, -1, -1]

    count += 1
    c = 0
    for i in range(1, M + 1):
        if shark[i][0] != -1:
            c += 1
        if c > 1:
            break
    if c == 1:
        break

print(count)