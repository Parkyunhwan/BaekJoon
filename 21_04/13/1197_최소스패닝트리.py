V, E = map(int, input().split())
parent = [x for x in range(V + 1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

graph = []
result = 0
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph.append([cost, a, b])
graph.sort()

for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)