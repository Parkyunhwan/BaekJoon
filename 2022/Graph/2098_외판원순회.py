import sys
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))

d = [[sys.maxsize for _ in range(1 << N)] for _ in range(N)]
all_visited = (1 << N) - 1

def tps(node, visited):
    if all_visited == visited:
        return sys.maxsize if W[node][0] == 0 else W[node][0]

    if d[node][visited] != sys.maxsize:
        return d[node][visited]
    for nextCity in range(N):
        if visited & (1 << nextCity):
            continue
        if not W[node][nextCity]:
            continue
        else:
            d[node][visited] = min(d[node][visited], tps(nextCity, (visited | (1 << nextCity))) + W[node][nextCity])
    return d[node][visited]

print(tps(0, 1))