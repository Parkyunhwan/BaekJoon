n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
arr = []
g_n = 0

def dfs(depth, col):
    if depth == n:
        return 0
    if dp[depth][col] != -1:
        return dp[depth][col]

    max_value = 0
    for d in range(-1, 0, 1):
        next_col = col + d
        if next_col < 0 or next_col >= n:
            continue
        max_value = max(dfs(depth + 1, next_col) + arr[depth][col], max_value)
    dp[depth][col] = max_value
    return dp[depth][col]

def solution(a, n):
    arr = a
    g_n = n
    for i in range(n):
        dfs(0, i)
    print(min(dp[n - 1]), max(dp[n - 1]))


solution(a, n)
