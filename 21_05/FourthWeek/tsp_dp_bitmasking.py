n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
cache = [[0] * 17 for _ in range(2 ** 16)]
def TSP(curr, visited):
    if visited == (1 << n) - 1:
        return dist[curr][0]

    ret = cache[visited][curr]
    if ret != 0:
        return ret
    ret = 1e9
    for i in range(n):
        if visited & (1 << i): # 다음 정점을 이미 방문했다면
            continue
        if dist[curr][i] == 0: # 갈 수 있는 간선이 없다면..
            continue
        ret = min(ret, TSP(i, visited | (1 << i)) + dist[curr][i])
    return ret

print(TSP(0, 1))