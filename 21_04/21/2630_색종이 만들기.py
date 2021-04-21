N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def check_samecolor(x, y, size):
    color = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                return False
    return True


def partition(x, y, size):
    global white, blue
    if size == 1:
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1
        return

    if check_samecolor(x, y, size):
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1
    else:
        half_size = size // 2
        partition(x, y, half_size)
        partition(x, y + half_size, half_size)
        partition(x + half_size, y, half_size)
        partition(x + half_size, y + half_size, half_size)


partition(0, 0, N)
print(white)
print(blue)