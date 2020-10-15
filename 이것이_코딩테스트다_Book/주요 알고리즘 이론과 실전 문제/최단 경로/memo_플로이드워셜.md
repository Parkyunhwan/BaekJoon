# 플로이드 워셜 알고리즘

모든 지점에서 다른 모든 지점까지 최단 경로를 모두 구해야 하는 경우
단계 마다 N번의 단계를 수행하며, O(N^2) 연산을 통해 현재 노드르 거쳐가는 모든 경로를 고려한다.

플로이드 워셜 알고리즘은 다이나믹 프로그래밍이라는 특징이 있다.

* 점화식 => `D<a,b> = min(D<a,b>, D<a,k> + D<k,b>`

따라서, O(n-1P2) 는 O(N^2)이므로 이를 N번 반복하므로 시간복잡도는 O(N^3)이다.

### 플로이드 워셜 알고리즘 소스코드

```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
```

 