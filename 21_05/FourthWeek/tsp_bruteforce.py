n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
def TSP(path, visited, length):
    if len(path) == len(visited):
        return length + dist[path[-1]][0]
    ret = 1e9
    print(length)
    for i in range(n):
        if visited[i]:
            continue
        curr = path[-1]
        path.append(i)
        visited[i] = True
        ret = min(ret, TSP(path, visited, length + dist[curr][i]))
        visited[i] = False
        path.pop()

    return ret


path = [0]
visited[0] = True
print(TSP(path, visited, 0))