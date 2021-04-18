# 최소 스패닝 트리 문제 (MST)
N = int(input())
M = int(input())


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = [x for x in range(N + 1)]

result = 0
for i in range(len(graph)):
    cost, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)