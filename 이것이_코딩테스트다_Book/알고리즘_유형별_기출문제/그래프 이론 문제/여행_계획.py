# 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행 경로이다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 서로소 집합 자료구조를 사용
n, m = map(int, input().split())

# 부모 표시 배열 필수
parent = [0] * (n + 1)

# 자기 자신을 부모로
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: ## i와 j 가 연결인 입력인 경우
            union_parent(parent, i + 1, j + 1) # 부모를 연결시킴(union)

plan = list(map(int, input().split()))
result = True
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")