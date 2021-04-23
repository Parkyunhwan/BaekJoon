import heapq
V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
distance = [1e9] * (V + 1)
start = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, curr = heapq.heappop(q)
    if distance[curr] < dist:
        continue
    for val in graph[curr]:
        arrival, cost = val
        if distance[arrival] > dist + cost:
            distance[arrival] = dist + cost
            heapq.heappush(q, (dist + cost, arrival))

for i in range(1, V + 1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])



'''
    벨만 포드
    dp
'''
# V, E = map(int, input().split())
#
# graph = [[1e9] * (V + 1) for _ in range(V + 1)]
#
# start = int(input())
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u][v] = w
#
# for i in range(1, V + 1):
#     for j in range(1, V + 1):
#         if i == j:
#             graph[i][j] = 0
#
# for k in range(1, V + 1):
#     for i in range(1, V + 1):
#         for j in range(1, V + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for i in range(1, V + 1):
#     if graph[start][i] == 1e9:
#         print("INF")
#     else:
#         print(graph[start][i])



