# 신장 트리

* 그래프 알고리즘 문제로 자주 출제
* 하나의 그래프가 있을 때 `모든 노드를 포함`하면서 `사이클이 존재하지 않는 부분 그래프`
    1. 모든 노드 포함
    2. 사이클이 존재하지 않음
    
# 크루스칼 알고리즘

* 최소한의 비용으로 신장 트리를 찾는 `최소 신장 트리 알고리즘`
* 크루스칼을 통해 가장 적은 비용으로 모든 노드 연결 가능
> <순서>
>
    1. 간선 비용에 따라 오름차순으로 정렬 (정렬)
    2. 간선을 하나씩 확인하여 사이클이 있는지 검사 (사이클 검사)
        1. 사이클 발견 안될 시 최소 신장 트리에 포함
        2. 사이클 발견 시 최소 신장트리에 포함 안함
    3. 모든 간선에 대해 해당 과정 반복

* 최소 신장 트리의 간선의 개수는 `노드의 개수 -1` 이다.

### 크루스칼 알고리즘 소스코드
* 크루스칼 알고리즘은 간선의 개수가 `E`일 때 `O(ElogE)`의 시간 복잡도
* 크루스칼에서 가장 오래 걸리는 부분은 정렬이며 서로소 집합 알고리즘의 시간 복잡도는 매우 작으므로 무시한다.
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```