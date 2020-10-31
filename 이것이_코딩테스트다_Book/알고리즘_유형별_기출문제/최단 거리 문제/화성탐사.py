# ``` 2차원 다익스트라 ```
import heapq
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]

    distance[0][0] = arr[0][0]
    q = []
    heapq.heappush(q, ((0, 0), distance[0][0]))
    while q:
        now, dist = heapq.heappop(q)
        x, y = now
        if distance[x][y] < dist:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[nx][ny] > dist + arr[nx][ny]:
                distance[nx][ny] = dist + arr[nx][ny]
                heapq.heappush(q, ((nx, ny), distance[nx][ny]))
    for d in distance:
        print(d)

