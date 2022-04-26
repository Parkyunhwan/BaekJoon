from collections import Counter
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    elif b < a:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    parent = [0] * (N + 1)
    for i in range(len(parent)):
        parent[i] = i

    for i in range(1, N + 1):
        union_parent(parent, i, arr[i])
    count = 0
    cycle_visit = [False] * (N + 1)
    for i in range(1, N + 1):
        if find_parent(parent, i) == find_parent(parent, arr[i]):
            if not cycle_visit[find_parent(parent, i)]:
                count += 1
                cycle_visit[parent[i]] = True

    print(count)