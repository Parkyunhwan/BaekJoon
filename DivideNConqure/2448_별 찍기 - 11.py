n = int(input())

arr = [[' '] * 6500 for _ in range(3500)]

base = ["  *  ", " *  * ", "*****"]
print(base)
def divide(start_x, start_y, n):
    if n == 1:
        for i in range(3):
            for j in range(5):
                print(start_x, start_y)
                print(i, j)
                arr[start_x + i][start_y + j] = base[i][j]
        return
    divide(start_x, start_y + 3 * n // 2, n // 2)
    divide(start_x + 3 * n // 2, start_y, n // 2)
    divide(start_x + 3 * n // 2, start_y + 3 * n, n // 2)

divide(0, 0, n // 3)
for i in range(n):
    for j in range(2*n - 1):
        print(arr[i][j], end='')
    print()
