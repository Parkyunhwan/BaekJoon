N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
INF = 1e9
min_dist = INF

all_visited = ((1 << N) - 1)
def dfs(curr, visited_bit):
    if visited_bit == all_visited:
        if W[curr][0] != 0:
            return W[curr][0]
        else:
            return INF

    if dp[visited_bit][curr] != INF:
        return dp[visited_bit][curr]

    for i in range(N):
        if visited_bit & (1 << i) != 0:
            continue
        if W[curr][i] == 0:
            continue
        dp[visited_bit][curr] = min(dfs(i, visited_bit | (1 << i)) + W[curr][i], dp[visited_bit][curr])
    return dp[visited_bit][curr]

dp = [[INF] * N for _ in range(1 << N)]
print(dfs(0, 1))