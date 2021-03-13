n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, bi, bj, char):

    if check[i][j]:
        print('Yes')
        exit(0)

    check[i][j] = True
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if ni < 0 or ni >= n or nj < 0 or nj >= m or arr[ni][nj] != char:
            continue
        if ni == bi and nj == bj:
            continue

        dfs(ni, nj, i, j, char)
        # 방문한 점을 다시 지우지 않는 게 포인트..
        # 이전 값을 기억해둬서 싸이클을 검사하는 방법.

for i in range(n):
    for j in range(m):
        if not check[i][j]:
            char = arr[i][j]
            dfs(i, j, -1, -1, char)
print('No')