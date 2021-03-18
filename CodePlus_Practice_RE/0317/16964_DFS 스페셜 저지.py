from collections import defaultdict

n = int(input())

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))
check = [False] * (n + 1)

def dfs(index):
    global k

    for _ in range(len(graph[index])):
        if order[k] in graph[index]:
            if not check[order[k]]:
                check[order[k]] = True
                val = order[k]
                k += 1
                if len(order) == k:
                    print(1)
                    exit(0)
                dfs(val)

if order[0] != 1:
    print(0)
    exit(0)

check[1] = True

k = 1
dfs(1)

print(0)