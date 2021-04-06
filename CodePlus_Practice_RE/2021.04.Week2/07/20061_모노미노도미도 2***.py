N = int(input())
# 1 : (1, 1), 2 : (1, 2), 3 : (2, 1)

red = [[0] * 4 for _ in range(4)]

blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]


def check_block(i, j, t, color):
    if color == 0:
        if t == 1:
            if blue[i][j] != 0:
                return False
            else:
                blue[i][j] = 1
                return True
        elif t == 2:
            if j + 1 == 6:
                return False
            if blue[i][j] != 0 and blue[i][j + 1] != 0:
                return False
            else:
                blue[i][j] = 1
                blue[i][j + 1] = 1
                return True
        elif t == 3:
            if i + 1 == 4:
                return False
            if blue[i][j] != 0 and blue[i + 1][j] != 0:
                return False
            else:
                blue[i][j] = 1
                blue[i + 1][j] = 1
                return True

    if color == 1:
        if t == 1:
            if green[i][j] != 0:
                return False
            else:
                green[i][j] = 1
                return True
        elif t == 2:
            if j + 1 == 4:
                return False
            if green[i][j] != 0 and green[i][j + 1] != 0:
                return False
            else:
                green[i][j] = 1
                green[i][j + 1] = 1
                return True
        elif t == 3:
            if i + 1 == 6:
                return False
            if green[i][j] != 0 and green[i + 1][j] != 0:
                return False
            else:
                green[i][j] = 1
                green[i + 1][j] = 1
                return True

def check_score():
    for j in range(5, 1, -1):
        flag = True
        for i in range(4):
            if blue[i][j] != 1:
                flag = False
                break
        if flag

for _ in range(N):
    t, x, y = map(int, input().split())

    i, j = x, y
    if t == 1:
        j = 5
    elif t == 2:
        i = 5
    while True:
        if check_block(i, j, t, 0):
            break
        if t == 1:
            j -= 1
        elif t == 2:
            i -= 1

    check_score()