from collections import defaultdict
N = int(input())
ss = int(input())


def infection(now):
    computers[now] = 1
    for node in graph[now]:
        if computers[node] == 0:
            computers[node] = 1
            infection(node)

graph = defaultdict(list)
computers = [0] * (N + 1)
for _ in range(ss):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

infection(1)

print(computers.count(1) - 1)
