# 최단 경로
가장 짧은 경로를 찾는 알고리즘 (`길찾기 문제`)
* 한 지점에서 다른 특정 지점 까지의 최단 경로
* 모든 지점에서 다른 모든 지점까지의 최단 경로

학부 수준에서 사용하는 최단 거리 알고리즘
* 다익스트라 
* 플로이드 워셜
* 벨만 포드

다익스트라, 플로이드 워셜이 코테에서 가장 많이 출제된다.

또한 최단 경로는 그리디와 다이나믹 프로그래밍의 한 종류이다.

### 다익스트라 최단 경로 알고리즘

여러개의 노드 중에서 특정한 노드에서 출발해 다른 노드로 가는 `각각`의 최단 경로를 구해주는 알고리즘

* 음의 간선이 없어야 한다.
* 매번 가장 적은 비용의 노드를 선택 (그리디 알고리즘)

> 순서

    1. 출발 노드 설정
    2. 최단 거리 테이블 초기화
    3. 방문하지 않은 노드 중 가장 짧은 노드 선택
    4. 다른 노드로 가능 비용을 계산해 최단 거리 테이블 갱신
    5. '3'번과 '4'번과정 반복

1차원 배열에 최단 거리를 정보를 저장해두고 계속 갱신한다.

다익스트라 알고리즘은 구현하기 쉽지만 느리게 동작하는 것과 `구현하기
까다롭지만 더 빠르게 동작하는 코드(방법 2)`가 있다고 한다.

그 중에서 우리는 시험을 준비하기 때문에 `방법 2`를 외워야 한다!

### 방법 1. 간단한 다익스트라

* O(V^2) => 각 단계마다 방문하지 않은 노드 중 가장 짧은 노드를 선택하기 위해 모든 노드 순차탐색
* 최단 거리가 가장 짧은 노드 구하기 X 현재 노드와 연결된 노드
```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

### 방법2. 개선된 다익스트라 알고리즘
    
* O(ElogV)를 보장. 힙 자료구조를 통해 최단 거리 노드를 O(logV)만에 찾음
* 파이썬 기본적으로 최소힙(heapq) , 음수 부호를 이용해 최대힙으로 사용 가능
* 현재 가장 가까운 노드를 저장하고 빠르게 찾기 위해 우선순위 큐 사용

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
 