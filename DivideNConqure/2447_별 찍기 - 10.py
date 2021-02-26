n = int(input())

arr = [[' '] * n for _ in range(n)]

def divide(start_x, start_y, n):
    if n == 1:
        arr[start_x][start_y] = '*'
        return
    div = n // 3
    for i in range(3):
        for j in range(3):
            x, y = start_x + div * i, start_y + div * j
            if i == 1 and j == 1:
                continue
            divide(x, y, div)

divide(0, 0, n)
for val in arr:
    for v in val:
        print(v, end='')
    print()
