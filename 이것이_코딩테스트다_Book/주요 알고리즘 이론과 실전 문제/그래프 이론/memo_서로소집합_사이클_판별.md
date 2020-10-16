# 그래프 이론

크루스칼 알고리즘(Kruskal Algorithm)은 그리디 알고리즘

위상 정렬 알고리즘(Topology Algorithm) 큐 or 스택 자료구조 사용

### 그래프의 구현 방식

1. 인접 행렬 : 2차원 배열을 사용하는 방식
    * 메모리 O(V^2), 탐색 O(1)
2. 인접 리스트 : 리스트를 사용하는 방식
    * * 메모리 O(E), 탐색 O(V)
    
ex) 플로이드 워셜 => 인접 행렬, 다익스트라 => 인접 리스트

## 서로소 집합
`공통원소`가 없는 두 집합을 말한다.

서로소 집합 자료구조는 몇몇 그래프 알고리즘에서 중요하게 사용된다.
* 서로소 집합 자료구조
    * 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
    
* `union()` : 2개의 원소가 포함된 집합을 하나의 집합으로 합침 
* `find()` : 특정한 원소가 속한 집합이 어떤 집합인지 알림

=> `서로소 집합 자료구조 == union-find 자료구조`

### 기본적인 서로소 집합 소스코드
* `find()`함수 실행 시 O(V)의 시간이 걸려서 `find()`를 E번 사용한다면 O(VE)가 되어 비효율적이다.
* 이러한 `find()`함수를 `경로 압축`을 통해 시간 복잡도를 개선시킬 수 있다.
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```
### 경로 압축 기법 소스코드
* `find()` 값을 재귀적으로 호출한 뒤 부모 테이블 값을 갱신하는 기법
* O(V+MlogV)의 시간 복잡도 걸리므로 이정도면 **코딩테스트**에선 충분하다.
* 기존 `find()`함수를 다음과 같이 변경한다.

```python
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```
### 사이클 판별

* 무방향 그래프의 사이클 판별 시에 서로소 집합을 이용할 수 있다.
* 방향 그래프는 DFS를 이용해 사이클 판별을 할 수 있다.


* 밑의 코드 처럼
```python
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료 (루트 노드가 같은 경우)
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union)수행
    else:
        union_parent(parent, a, b)
```


