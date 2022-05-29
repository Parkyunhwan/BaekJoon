from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
dic = defaultdict(list)
for _ in range(n - 1):
    a, b, cost = map(int, input().split())
    dic[a].append([b, cost])
    dic[b].append([a, cost])

distance = [-1] * (n + 1)
def dfs(curr):
    for next, cost in dic[curr]:
        if distance[next] == -1:
            distance[next] = distance[curr] + cost
            dfs(next)

dfs(1)
max_value = -1
max_vertex = []
distance[1] = 0
for i in range(1, n + 1):
    value = distance[i]
    if value > max_value:
        max_value = value
        max_vertex = [i, value]

distance = [-1] * (n + 1)
max_value = -1
distance[max_vertex[0]] = 0
dfs(max_vertex[0])
max_vertex = [max_vertex[0], 0]
for i in range(1, n + 1):
    value = distance[i]
    if value > max_value:
        max_value = value
        max_vertex = [i, value]
print(max_vertex[1])

# 부모는 있는데 자식은 없는 것 - 리프노드
