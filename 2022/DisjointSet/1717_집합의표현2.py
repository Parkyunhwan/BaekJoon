import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())

parent = [x for x in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(parent, a, b)
    else:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")