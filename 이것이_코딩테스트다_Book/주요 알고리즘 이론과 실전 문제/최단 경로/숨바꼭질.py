import bisect
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

INF = int(1e9)
distance = [INF]*(n+1)
q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
max_node = 0
max_distance = 0
result = 0
for d in distance:
    print(d)
for i in range(1, n+1):
    if distance[i] == INF:
        continue
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = 1
    elif max_distance == distance[i]:
        result += 1
print(max_node, max_distance, result)