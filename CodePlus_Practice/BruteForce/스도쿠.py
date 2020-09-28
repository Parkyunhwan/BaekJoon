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

#my solve
import sys


def solve(index):
    if index == len(zero):
        for com in arr:
            for c in com:
                print(c, end=" ")
            print()
        sys.exit(0)
    sel = zero[index]
    x = sel[0]; y = sel[1]
    # 가로 세로

    for val in range(1, 10):
        flag = True
        if val in arr[x]:
            continue
        for k in range(9):
            if arr[k][y] == val:
                flag = False
                break
        if flag is False:
            continue

        for i in range(3):
            for j in range(3):
                start_x = int((x//3)*3); start_y = int((y//3)*3)
                if val == arr[start_x + i][start_y + j]:
                    flag = False
                    continue
        if flag is True:
            arr[x][y] = val
            solve(index+1)
            arr[x][y] = 0


arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append((i, j))
solve(0)


