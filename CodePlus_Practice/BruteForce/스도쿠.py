# https://dojinkimm.github.io/problem_solving/2019/10/16/boj-2580-sudoku.html
# velog
def horizontal(y, n):
    if n in sudoku[y]:
        return False
    return True


def vertical(x, n):
    for i in range(9):
        if sudoku[i][x] == n:
            return False
    return True


def bythree(y, x, n):
    ny = (y // 3) * 3
    nx = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[ny + i][nx + j] == n:
                return False
    return True


def possible(loc, n):
    return horizontal(loc[0],n) and vertical(loc[1],n) and bythree(loc[0],loc[1],n)

def DFS(index):
    if len(zeros) == index:
        for r in sudoku:
            for k in r:
                print(k, end=" ")
            print()
        exit(0)
    else:
        for i in range(1, 10):
            loc = zeros[index]
            y = loc[0]
            x = loc[1]
            if possible(loc, i):
                sudoku[y][x] = i
                DFS(index + 1)
                sudoku[y][x] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
DFS(0)
