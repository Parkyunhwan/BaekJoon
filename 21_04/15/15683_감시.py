'''

-> https://jaimemin.tistory.com/1070 (이 방법으로 풀어보기)


'''

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# number = []
#
#
# for i in range(N):
#     for j in range(M):
#         if 1 <= arr[i][j] <= 5:
#             number.append([arr[i][j], i, j])
#
#
# def fill_direction(x, y, dir):
#     if dir == 0:
#         while y + 1 < M and arr[x][y + 1] != 6:
#             arr[x][y + 1] = -1
#             y = y + 1
#     elif dir == 1:
#         while x + 1 < N and arr[x + 1][y] != 6:
#             arr[x + 1][y] = -1
#             x = x + 1
#     elif dir == 2:
#         while y - 1 >= 0 and arr[x][y - 1] != 6:
#             arr[x][y - 1] = -1
#             y = y - 1
#     elif dir == 3:
#         while x - 1 >= 0 and arr[x - 1][y] != 6:
#             arr[x - 1][y] = -1
#             x = x - 1
#
#
# def fill_arr(cctv_num, x, y, dir):
#     if cctv_num == 1:
#         fill_direction(x, y, dir)
#     elif cctv_num == 2:
#         if dir == 0:
#             fill_direction(x, y, 0)
#             fill_direction(x, y, 2)
#         elif dir == 1:
#             fill_direction(x, y, 1)
#             fill_direction(x, y, 3)
#     elif cctv_num == 3:
#         if dir == 0:
#             fill_direction(x, y, 0)
#             fill_direction(x, y, 3)
#         elif dir == 1:
#             fill_direction(x, y, 1)
#             fill_direction(x, y, 0)
#         elif dir == 2:
#             fill_direction(x, y, 2)
#             fill_direction(x, y, 1)
#         elif dir == 3:
#             fill_direction(x, y, 3)
#             fill_direction(x, y, 2)
#     elif cctv_num == 4:
#         if dir == 0:
#             fill_direction(x, y, 0)
#             fill_direction(x, y, 3)
#             fill_direction(x, y, 2)
#         elif dir == 1:
#             fill_direction(x, y, 1)
#             fill_direction(x, y, 0)
#             fill_direction(x, y, 3)
#         elif dir == 2:
#             fill_direction(x, y, 2)
#             fill_direction(x, y, 1)
#             fill_direction(x, y, 0)
#         elif dir == 3:
#             fill_direction(x, y, 3)
#             fill_direction(x, y, 2)
#             fill_direction(x, y, 1)
#     else:
#         fill_direction(x, y, 3)
#         fill_direction(x, y, 2)
#         fill_direction(x, y, 1)
#         fill_direction(x, y, 0)
#
#
# def examine_arr():
#     global mn
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 count += 1
#     if mn > count:
#         mn = count
#
# def dfs(idx):
#     global arr
#
#     if idx == len(number):
#         examine_arr()
#         return
#
#     cctv_num, x, y = number[idx]
#     back_arr = [a[:] for a in arr]
#     for dir in range(4):
#         if cctv_num == 2 and dir >= 2:
#             continue
#         elif cctv_num == 5 and dir >= 1:
#             continue
#         fill_arr(cctv_num, x, y, dir)
#         dfs(idx + 1)
#         arr = [b[:] for b in back_arr]
#
# mn = 1e9
# dfs(0)
# print(mn)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
croom = [a[:] for a in arr]
visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
cctv = []
angle = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
mn = 1e9
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append([i, j])

        if arr[i][j] == 1:
            visited[i][j][0] = True
        elif arr[i][j] == 2:
            visited[i][j][0] = True
            visited[i][j][2] = True
        elif arr[i][j] == 3:
            visited[i][j][0] = True
            visited[i][j][3] = True
        elif arr[i][j] == 4:
            visited[i][j][0] = True
            visited[i][j][2] = True
            visited[i][j][3] = True
        elif arr[i][j] == 5:
            visited[i][j][0] = True
            visited[i][j][1] = True
            visited[i][j][2] = True
            visited[i][j][3] = True


def fill_block():
    global croom
    for i in range(len(cctv)):
        x, y = cctv[i]
        for j in range(4):
            if visited[x][y][j]:
                nx = x + dx[(angle[i] + j) % 4]
                ny = y + dy[(angle[i] + j) % 4]
                while True:
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        break
                    if croom[nx][ny] == 6:
                        break
                    if croom[nx][ny] == 0:
                        croom[nx][ny] = -1

                    nx += dx[(angle[i] + j) % 4]
                    ny += dy[(angle[i] + j) % 4]

def count_blindspot():
    count = 0
    for i in range(N):
        for j in range(M):
            if croom[i][j] == 0:
                count += 1
    return count


def dfs(idx):
    global mn, croom
    if idx == len(cctv):
        fill_block()
        mn = min(mn, count_blindspot())
        for i in range(N):
            for j in range(M):
                croom[i][j] = arr[i][j]
        return
    for i in range(4):
        angle.append(i)
        dfs(idx + 1)
        angle.pop()

dfs(0)
print(mn)