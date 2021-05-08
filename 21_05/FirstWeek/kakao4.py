import heapq
ggraph = []
trap = []
graphFake = []
ge = 0
mn = 1e9


def dfs(curr, distance_cost):
    global graphFake, mn
    fake = 0
    if curr == ge:
        mn = min(distance_cost, mn)
        return
    if curr in trap:
        if not graphFake[curr]:
            graphFake[curr] = True
            fake = 1
        else:
            graphFake[curr] = False

    for val in ggraph[curr][fake]:
        ne, cost = val
        dfs(ne, distance_cost + cost)

def solution(n, start, end, roads, traps):
    global ggraph, trap, ge, graphFake
    trap = traps
    ge = end
    graph = [[[] for _ in range(2)] for _ in range(n + 1)]
    graphFake = [False] * (n + 1)
    distance = [1e9] * (n + 1)
    for road in roads:
        s, e, cost = road
        graph[s][0].append([e, cost])
        graph[e][1].append([s, cost])


    ggraph = graph
    dfs(start, 0)
    print(mn)
    return mn

solution(10, 1, 10, [[1, 2, 2], [3, 2, 3],[1, 2, 2], [3, 4, 3],[1, 2, 2], [9, 2, 3],[1, 2, 2], [8, 2, 3],[7, 2, 2], [3, 7, 3]], [3, 7, 2])