'''
    각각을 시작점으로 잡고 외판원 순회시작
'''
N = int(input())
cost_map = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = 1e9


def tsp(start, curr, sm):
    global result
    if curr == start and False not in visited:
        result = min(result, sm)
        return
    if visited[curr]:
        return
    visited[curr] = True

    for i in range(N):
        if cost_map[curr][i] == 0:
            continue
        else:
            tsp(start, i, sm + cost_map[curr][i])
    visited[curr] = False


for i in range(N):
    tsp(i, i, 0)

print(result)