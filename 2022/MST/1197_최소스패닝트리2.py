import heapq
import sys
V, E = map(int, input().split())

Edge = []
INF = sys.maxsize
distance = [INF] * (V + 1)
for _ in range(E):
    A, B, C = map(int, input().split())
    Edge.append((C, A, B))

Edge.sort()

parent = [x for x in range(V + 1)]
parent[0] = 1
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


result = 0
for edge in Edge:
    cost, a, b = edge
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        continue
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    result += cost

print(parent)
print(result)
# 크루스칼 알고리즘은 최솟값 간선 + 그리디 + find-union으로 구한다.