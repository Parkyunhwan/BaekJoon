def solution(rows, columns, queries):
    # arr 입력
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1

    answer = []
    for x1, y1, x2, y2 in queries:
        x, y = x1 - 1, y1 - 1
        tmp = arr[x + 1][y]
        minN = tmp
        while y != y2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += 1
        while x != x2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += 1
        while y != y1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += -1
        while x != x1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += -1

        answer.append(minN)

    return answer


def solution(rows, columns, queries):
    # arr 입력
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1

    answer = []
    for x1, y1, x2, y2 in queries:
        x, y = x1 - 1, y1 - 1
        tmp = arr[x + 1][y]
        minN = tmp
        while y != y2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += 1
        while x != x2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += 1
        while y != y1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += -1
        while x != x1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += -1

        answer.append(minN)

    return answer


def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = rows * i + j + 1

    for query in queries:
        sx, sy, ex, ey = query
        sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1

        tmp = arr[sx][sy]
        min_value = tmp

        curr_x, curr_y = sx, sy
        while curr_x != ex:
            arr[curr_x][curr_y] = arr[curr_x + 1][curr_y]
            min_value = min(min_value, arr[curr_x][curr_y])
            curr_x += 1
        while curr_y != ey:
            arr[curr_x][curr_y] = arr[curr_x][curr_y + 1]
            min_value = min(min_value, arr[curr_x][curr_y])
            curr_y += 1
        while curr_x != sx:
            arr[curr_x][curr_y] = arr[curr_x - 1][curr_y]
            min_value = min(min_value, arr[curr_x][curr_y])
            curr_x -= 1
        while curr_y != sy:
            arr[curr_x][curr_y] = arr[curr_x][curr_y - 1]
            min_value = min(min_value, arr[curr_x][curr_y])
            curr_y -= 1
        arr[sx][sy + 1] = tmp
        min_value = min(min_value, tmp)
        answer.append(min_value)

    return answer