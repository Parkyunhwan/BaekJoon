# Union-find 구현 문 (경로 압축 방식 사용 - 모두 루트 노드를 가르키게 됨)

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("yes")
        else:
            print("No")