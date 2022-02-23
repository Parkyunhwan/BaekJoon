import sys
from collections import defaultdict
import heapq
V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
# graph = defaultdict(list)
graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
for _ in range(E):
    v1, v2, cost = map(int, input().split())
    graph[v1].append([v2, cost])

def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        curr_cost, curr = heapq.heappop(q)
        if dist[curr] < curr_cost:
            continue
        for j in graph[curr]:
            next, next_cost = j[0], j[1]
            if dist[next] > curr_cost + next_cost:
                dist[next] = curr_cost + next_cost
                heapq.heappush(q, (curr_cost + next_cost, next))

dijkstra2(K)
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, V + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if dist[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(dist[i])









