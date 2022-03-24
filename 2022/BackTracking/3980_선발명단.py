import sys
input = sys.stdin.readline
C = int(input())


def dfs(idx, sum_value):
    global result
    if idx == 11:
        result = max(result, sum_value)
        return

    for j in range(11):
        if s[idx][j] > 0:
            if visited[j]:
                continue
            visited[j] = True
            dfs(idx + 1, sum_value + s[idx][j])
            visited[j] = False

result = 0
for _ in range(C):
    visited = [False] * 11
    s = []
    result = 0
    for _ in range(11):
        s.append(list(map(int, input().split())))
    dfs(0, 0)
    print(result)

