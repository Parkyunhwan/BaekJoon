dx = [1, 0]
dy = [0, 1]
row = [[False] * 9 for _ in range(10)]
col = [[False] * 9 for _ in range(10)]
tile = [[False] * 10 for _ in range(10)]
square = [[False] * 3 for _ in range(3)]
def rangeCheck(x, y):
    if x < 0 or x >= 9 or y < 0 or y >= 9:
        return False
    else:
        return True

def makeVisit(x, y, i, j, C, bol):
    tile[i][j] = bol
    tile[j][i] = bol

    if C == 'G':
        row[x][i] = row[x][j] = bol
        col[y][i] = col[y + 1][j] = bol
        square[x // 3][y // 3][i] = square[x // 3][(y + 1) // 3][j] = bol

        if bol:
            sudoku[x][y] = i
            sudoku[x][y + 1] = j
        else:
            sudoku[x][y] = 0
            sudoku[x][y + 1] = 0
    else:
        row[x][i] = row[x + 1][j] = bol
        col[y][i] = row[y][j] = bol
        square[x // 3][y // 3][i] = square[(x + 1) // 3][y // 3][j] = bol

        if bol:
            sudoku[x][y] = i
            sudoku[x + 1][y] = j
        else:
            sudoku[x][y] = 0
            sudoku[x + 1][y] = 0
def dfs(index):
    if index == 81:
        flag = True
        print("Puzzle {}".format(Tc))
        return

    x = index / 9
    y = index % 9

    if sudoku[x][y] != 0:
        dfs(index + 1)
    else:
        if y <= 7 and sudoku[x][y + 1] == 0:
            for i in range(9):
                for j in range(i + 1, 9):
                    if not tile[i][j]:
                        if check(x, y, i, j, 'G'):
                            makeVisit(x, y, i, j, 'G', true)
                            dfs(idx + 2)
                            makeVisit(x, y, i, j, 'G', false)


while True:
    n = int(input())
    if n == 0:
        break
    sudoku = [[0] * 9 for _ in range(9)]
    for _ in range(n):
        arr = input().split()
        pos1 = list(arr[1])
        pos2 = list(arr[3])

        print(arr)
        pos1[0], pos1[1] = int(ord(pos1[0]) - ord('A')), int(pos1[1]) - 1
        pos2[0], pos2[1] = int(ord(pos2[0]) - ord('A')), int(pos2[1]) - 1
        print(pos1, pos2)
        sudoku[pos1[0]][pos1[1]] = int(arr[0])
        sudoku[pos2[0]][pos2[1]] = int(arr[2])
    arr = input().split()
    for i, com in enumerate(arr):
        li = list(com)
        x, y = li[0], li[1]
        x, y = int(ord(x) - ord('A')), int(y) - 1
        sudoku[x][y] = i + 1
    print(sudoku)

