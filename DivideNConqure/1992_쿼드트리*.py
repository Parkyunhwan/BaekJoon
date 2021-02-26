# https://suri78.tistory.com/68
n = int(input())

arr = [input() for _ in range(n)]


def check(x, y, n):
    val = arr[x][y]
    for i in range(n):
        for j in range(n):
            if arr[x + i][y + j] != val:
                return False
    return True


def divide(start_x, start_y, n):
    print('(', end='')
    div = n // 2
    for i in range(2):
        for j in range(2):
            x, y = start_x + div * i, start_y + div * j
            if check(x, y, div):
                print(arr[x][y], end='')
            else:
                divide(x, y, div)
    print(')', end='')
    return


# if check(0, 0, n):
#     print(arr[0][0], end='')
#     exit(0)

divide(0, 0, n)