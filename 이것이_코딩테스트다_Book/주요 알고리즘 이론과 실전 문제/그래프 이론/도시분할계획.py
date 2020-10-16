n, m = map(int, input().split())
edges = []
parent = [x for x in range(0, n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


i = 0
sm = 0
mx = -1
vertex = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        sm += cost
        union_parent(parent, a, b)
        mx = cost
print(sm-mx)
