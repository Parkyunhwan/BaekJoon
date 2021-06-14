import sys
read = sys.stdin.readline


def solve():
    N, M = map(int, read().split())

    dp = [[0] * (M+1)] + [[0] + list(map(int, read().split())) for _ in range(N)]

    for r in range(1, N+1):
        for c in range(2, M+1):
            dp[r][c] += dp[r][c-1]

    for r in range(2, N+1):
        for c in range(1, M+1):
            dp[r][c] += dp[r-1][c]

    K = int(read().rstrip())
    for _ in range(K):
        r1, c1, r2, c2 = map(int, read().split())
        print(dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1])
