from collections import defaultdict, deque
import heapq
import math
N, M = map(int, input().split())
graph = defaultdict(list)


def find_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

def cal_cost(graph1, graph2):
    x1, y1 = graph1
    x2, y2 = graph2
    return math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))

visited = [[False] * (N + 1) for _ in range(N + 1)]
parent = [x for x in range(N + 1)]
for i in range(1, N + 1):
    x, y = list(map(int, input().split()))
    parent[i] = i
    graph[i] = [x, y]

for i in range(M):
    x, y = list(map(int, input().split()))
    visited[x][y] = True
    union(parent, x, y)

q = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        if not visited[i][j]:
            visited[i][j] = True
            heapq.heappush(q, [cal_cost(graph[i], graph[j]), i, j])

min_cost = 0
while q:
    cost, x, y = heapq.heappop(q)
    if union(parent, x, y):
        min_cost += cost

print('%.2f' %min_cost)