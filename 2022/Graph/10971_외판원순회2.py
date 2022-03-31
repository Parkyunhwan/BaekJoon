N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))

d = [[0 for _ in range(N)] for _ in range(N)]
visited = [False] * N
start = 0
result = 1e9
def travle(city, distanceSum):
    global result
    if city == start and False not in visited:
        result = min(result, distanceSum)
    if visited[city]:
        return
    visited[city] = True
    for i in range(N):
        # 방문체크부터
        if W[city][i] == 0:
            continue
        else:
            travle(i, distanceSum + W[city][i])
    visited[city] = False

travle(0, 0)
print(result)








