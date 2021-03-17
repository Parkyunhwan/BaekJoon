from collections import defaultdict
from collections import deque
n = int(input())

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))

visited = [False] * (n + 1)
q = deque()
k = 0
q.append(order[k])
k += 1

while q:
    curr = q.popleft()
    if k == len(order):
        break
    i = 0
    while i < len(graph[curr]) and k < len(order):
        if order[k] in graph[curr]:
            if not visited[order[k]]:
                visited[order[k]] = True
                q.append(order[k])
                k += 1
            i += 1
        else:
            print(0)
            exit(0)

print(1)