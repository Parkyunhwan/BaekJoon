N = int(input())

map = [[0 for _ in range(N)] for _ in range(N)]
count = 0
def solve():
    dfs(0)


def isPossible(row, col):
    for i in range(N):
        if map[i][col] == 1:
            return False

    # row와 col 하나라도 0이 될때까지 검사
    pr = row - 1
    pc = col - 1
    while pr >= 0 and pc >= 0:
        if map[pr][pc] == 1:
            return False
        pr -= 1
        pc -= 1

    # row와 col 하나라도 0이 될때까지 검사
    pr = row - 1
    pc = col + 1
    while pr >= 0 and pc < N:
        if map[pr][pc] == 1:
            return False
        pr -= 1
        pc += 1

    return True


def dfs(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N):
        if isPossible(row, col):
            map[row][col] = 1
            dfs(row + 1)
            map[row][col] = 0

solve()
print(count)