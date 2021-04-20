# import copy
# SHARK = -2
# NOTTHING = -2
# arr = [[[0] * 2 for _ in range(4)] for _ in range(4)]
#
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, -1, -1, -1, 0, 1, 1, 1]
#
# fish = [[0] * 3 for _ in range(17)]
# for i in range(4):
#     input_arr = list(map(int, input().split()))
#
#     for j in range(4):
#         arr[i][j][0] = input_arr[2*j]
#         arr[i][j][1] = input_arr[2*j + 1]
#         fish[arr[i][j][0]] = [i, j, arr[i][j][1]]
#
# fish[arr[0][0][0]] = [NOTTHING, NOTTHING, NOTTHING]
# shark = [0, 0, arr[0][0][1], arr[0][0][0]]  #  x, y, direction, score
# arr[0][0] = [SHARK, arr[0][0][1]]
#
# def select_candidate(cand):
#     x, y, dir, score = shark
#     nx, ny = x + dx[dir - 1], y + dy[dir - 1]
#     while 0 <= nx < 4 and 0 <= ny < 4:
#         if arr[nx][ny][0] != NOTTHING:
#             cand.append([nx, ny])
#         nx, ny = nx + dx[dir - 1], ny + dy[dir - 1]
#     return cand
#
#
# def move_fish():
#     for i in range(1, 17):
#         if fish[i][0] == NOTTHING:
#             continue
#         x, y, dir = fish[i]
#         for _ in range(8):
#             nx, ny = x + dx[dir - 1], y + dy[dir - 1]
#             if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or arr[nx][ny][0] == SHARK:
#                 dir += 1
#                 dir %= 8
#                 continue
#
#             arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
#             fish[i] = [nx, ny, dir]
#             fish[arr[x][y][0]] = [x, y, arr[x][y][1]]
#             break
#
#
# mx = 0
# def solve():
#     global mx, shark, arr, fish
#     print(shark)
#
#     move_fish()
#     for row in arr:
#         print(row)
#     cand = []
#     cand = select_candidate(cand)
#     if len(cand) == 0:
#         mx = max(mx, shark[3])
#         return
#     back = [a[:] for a in arr]
#     bfish = copy.deepcopy(fish)
#     bshark = copy.deepcopy(shark)
#     print("asdfafse {}".format(cand))
#     for can in cand:
#         x, y = can
#         shark = [x, y, arr[x][y][1], shark[3] + arr[x][y][0]]
#         arr[x][y] = [NOTTHING, NOTTHING]
#         print("val %d" % (shark[3] + arr[x][y][0]))
#         solve()
#         shark = copy.deepcopy(bshark)
#         arr = [b[:] for b in back]
#         fish = copy.deepcopy(bfish)
# solve()
# print(mx)
#
import copy
SHARK = -1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def food(array, x, y):

    position = []
    direction = array[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
            position.append([nx, ny])
        x, y = nx, ny
    return position

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_fish(array, curr_x, curr_y):
    flag = False
    position = []
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        dir = array[x][y][1]
        for j in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                dir = (dir + 1) % 8
                continue
            if not (nx == curr_x and ny == curr_y):
                array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
                break
            dir = (dir + 1) % 8

def dfs(array, x, y, total):
    global answer

    array = copy.deepcopy(array)

    # 현재 x, y의 물고기를 상어가 먹음
    number = array[x][y][0]
    array[x][y][0] = SHARK # 상어 표시

    # 물고기 이동
    move_fish(array, x, y)

    # 상어의 이동 후보 추출
    result = food(array, x, y)
    answer = max(answer, total + number)
    for nx, ny in result:
        dfs(array, nx, ny, total + number)

if __name__ == "__main__":
    temp = [list(map(int, input().split())) for _ in range(4)]
    array = [[None] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]
    answer = 0
    dfs(array, 0, 0, 0)
    print(answer)