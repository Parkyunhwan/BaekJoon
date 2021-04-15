'''

-> https://jaimemin.tistory.com/1070 (이 방법으로 풀어보기)


'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

number = []


for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            number.append([arr[i][j], i, j])


def fill_direction(x, y, dir):
    if dir == 0:
        while y + 1 < M and arr[x][y + 1] != 6:
            arr[x][y + 1] = -1
            y = y + 1
    elif dir == 1:
        while x + 1 < N and arr[x + 1][y] != 6:
            arr[x + 1][y] = -1
            x = x + 1
    elif dir == 2:
        while y - 1 >= 0 and arr[x][y - 1] != 6:
            arr[x][y - 1] = -1
            y = y - 1
    elif dir == 3:
        while x - 1 >= 0 and arr[x - 1][y] != 6:
            arr[x - 1][y] = -1
            x = x - 1


def fill_arr(cctv_num, x, y, dir):
    if cctv_num == 1:
        fill_direction(x, y, dir)
    elif cctv_num == 2:
        if dir == 0:
            fill_direction(x, y, 0)
            fill_direction(x, y, 2)
        elif dir == 1:
            fill_direction(x, y, 1)
            fill_direction(x, y, 3)
    elif cctv_num == 3:
        if dir == 0:
            fill_direction(x, y, 0)
            fill_direction(x, y, 3)
        elif dir == 1:
            fill_direction(x, y, 1)
            fill_direction(x, y, 0)
        elif dir == 2:
            fill_direction(x, y, 2)
            fill_direction(x, y, 1)
        elif dir == 3:
            fill_direction(x, y, 3)
            fill_direction(x, y, 2)
    elif cctv_num == 4:
        if dir == 0:
            fill_direction(x, y, 0)
            fill_direction(x, y, 3)
            fill_direction(x, y, 2)
        elif dir == 1:
            fill_direction(x, y, 1)
            fill_direction(x, y, 0)
            fill_direction(x, y, 3)
        elif dir == 2:
            fill_direction(x, y, 2)
            fill_direction(x, y, 1)
            fill_direction(x, y, 0)
        elif dir == 3:
            fill_direction(x, y, 3)
            fill_direction(x, y, 2)
            fill_direction(x, y, 1)
    else:
        fill_direction(x, y, 3)
        fill_direction(x, y, 2)
        fill_direction(x, y, 1)
        fill_direction(x, y, 0)


def examine_arr():
    global mn
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    if mn > count:
        mn = count

def dfs(idx):
    global arr

    if idx == len(number):
        examine_arr()
        return

    cctv_num, x, y = number[idx]
    back_arr = [a[:] for a in arr]
    for dir in range(4):
        if cctv_num == 2 and dir >= 2:
            continue
        elif cctv_num == 5 and dir >= 1:
            continue
        fill_arr(cctv_num, x, y, dir)
        dfs(idx + 1)
        arr = [b[:] for b in back_arr]

mn = 1e9
dfs(0)
print(mn)



