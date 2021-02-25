n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

result = [0] * 3

def possible(start_x: int, start_y: int, n: int):
    temp = arr[start_x][start_y]
    for i in range(n):
        for j in range(n):
            if temp != arr[start_x + i][start_y + j]:
                return False
    return True


def divide(x, y, n):

    if possible(x, y, n):
        result[arr[x][y] + 1] += 1
    else:
        div = n // 3
        for i in range(3):
            for j in range(3):
                divide(x + i * div, y + j * div, div)
    return


divide(0, 0, n)

for i in range(3):
    print(result[i])