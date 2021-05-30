'''
    범위가 넓어서

'''
answer = []

def dfs(curr_v, hap, k, graph, visited):
    if hap > k:
        return
    if hap == k:
        if not visited[curr_v]:
            visited[curr_v] = True
            answer.append(curr_v)
        return
    for gh in graph[curr_v]:
        next_v, cost = gh
        dfs(next_v, hap + cost, k, graph, visited)

def solution(n, k, roads):
    graph = [[] * n for _ in range(n)]
    visited = [False] * n
    for road in roads:
        v1, v2, cost = road
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

    dfs(0, 0, k, graph, visited)

    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)
    return answer