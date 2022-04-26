import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())

parent = [x for x in range(n + 1)]


def find_parent(parent, a):
    if a == parent[a]:
        return a
    parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a =  find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isSameSet(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        return False
    return True

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(parent, a, b)
    else:
        if isSameSet(parent, a, b):
            print("YES")
        else:
            print("NO")