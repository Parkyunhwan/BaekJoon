# 플로이드 워셜 ㄱㄱ
# 최단 거리 문제는 그림으로 먼저 그려보고 푸는 것이 좋다.
# n의 범위가 100으로 매우 한정정이다. 따라서 시간복잡도는 10^2^3 = 10^6 = 100000 (십만번)
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


sm = graph[1][k] + graph[k][x]
if sm >= INF:
    print(-1)
else:
    print(sm)


