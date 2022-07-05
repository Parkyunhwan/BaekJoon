import sys
from collections import defaultdict
import heapq
V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

distance = [INF] * (V + 1)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, curr = heapq.heappop(q)

        if distance[curr] < dist:
            continue
        for ne_list in graph[curr]:
            next_v, cost = ne_list
            if dist + cost < distance[next_v]:
                distance[next_v] = dist + cost
                heapq.heappush(q, [distance[next_v], next_v])

dijkstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])








