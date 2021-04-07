'''
    https://jjangsungwon.tistory.com/54

    구현이안된다.. 어디서 틀렷을까?
'''
import copy
position = [[0] * 2 for _ in range(17)]
SHARK = -5
arr = []
for _ in range(4):
    tmp = []
    row_in = list(map(int, input().split()))
    for i in range(0, 8, 2):
        tmp.append([row_in[i], row_in[i + 1]])
    arr.append(tmp)

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def dfs(shark_x, shark_y, sea, sm):
    global mx
    # 1. 물고기 이동

    # 번호 위치 구하기
    for i in range(4):
        for j in range(4):
            num = sea[i][j][0]
            position[num] = [-1, -1]
            if num >= 1:
                position[num][0] = i
                position[num][1] = j

    for i in range(1, 17):
        x, y = position[i]
        if sea[x][y][0] < 1:
            continue
        num, dir = sea[x][y]
        nx, ny = x + dx[dir], y + dy[dir]
        idx = 0
        while nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or sea[nx][ny][0] == SHARK:
            dir += 1
            if dir == 9:
                dir = 1
            nx, ny = x + dx[dir], y + dy[dir]
            idx += 1
            if idx == 8:
                break
        if idx == 8:
            continue

        # 정상적인 값이라면 자리 교환
        tmp = sea[nx][ny]

        position[num] = [nx, ny]
        position[tmp[0]] = [x, y]

        sea[nx][ny] = sea[x][y]
        sea[x][y] = tmp

    # 상어의 식사
    shark_dir = sea[shark_x][shark_y][1]

    nx, ny = shark_x + dx[shark_dir], shark_y + dy[shark_dir]
    count = 0
    while 0 <= nx < 4 and 0 <= ny < 4:
        if sea[nx][ny][0] >= 1:
            back = copy.deepcopy(sea)
            score = sea[nx][ny][0]

            back[shark_x][shark_y] = [0, 0]
            back[nx][ny] = [SHARK, sea[nx][ny][1]]
            for row in back:
                print(row)
            print(sm, score, sm + score)
            print()
            dfs(nx, ny, back, sm + score)
            count += 1
        nx, ny = nx + dx[shark_dir], ny + dy[shark_dir]
    if count == 0:
        print("갱신")
        for row in sea:
            print(row)
        print(sm)
        print()
        mx = max(mx, sm)
        return

mx = 0
sm = arr[0][0][0]
arr[0][0] = [SHARK, arr[0][0][1]]
dfs(0, 0, arr, sm)
print(mx)