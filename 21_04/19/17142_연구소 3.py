'''
    벽이 있을 땐 시간체크 맵과 일반 맵을 따로두기.

    빈 벽의 갯수 == 방문한 위치의 갯수 이용하기.

'''
from collections import deque
WALL = -1
EMPTY = -2
ACTIVE = 0
INACTIVE = -3
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

virus_position = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = WALL
        elif arr[i][j] == 0:
            arr[i][j] = EMPTY
        elif arr[i][j] == 2:
            arr[i][j] = INACTIVE
            virus_position.append([i, j, INACTIVE])
back = [a[:] for a in arr]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_result = 1e9


def select_virus(idx):
    if idx == M:
        spread_virus()
        check_mintime()
        return
    for i in range(1, len(virus_position)):
        if virus_position[i][2] == ACTIVE:
            continue
        x, y = virus_position[i][0], virus_position[i][1]
        virus_position[i][2] = ACTIVE
        select_virus(idx + 1)
        virus_position[i][2] = INACTIVE


def spread_virus():
    global arr
    for virus in virus_position:
        if virus[2] == ACTIVE:
            q.append([virus[0], virus[1]])
            arr[virus[0]][virus[1]] = ACTIVE

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] != EMPTY and arr[nx][ny] != INACTIVE:
                continue
            arr[nx][ny] = arr[x][y] + 1
            q.append([nx, ny])

def check_mintime():
    global min_result, arr
    mx = 0
    flag = True
    for i in range(N):
        for j in range(N):
            if arr[i][j] == EMPTY:
                flag = False
                break
            if mx < arr[i][j] and back[i][j] != INACTIVE:
                mx = arr[i][j]
        if not flag:
            break
    if flag:
        min_result = min(min_result, mx)

    arr = [b[:] for b in back]

select_virus(0)

if min_result == 1e9:
    print(-1)
else:
    print(min_result)