N = int(input())
M = int(input())
parent = [x for x in range(N + 1)]

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

for i in range(1, N + 1):
    jlist = list(map(int, input().split()))
    for j in range(1, N + 1):
        val = jlist[j - 1]
        if val == 1:
            union(parent, i, j)


connected_info = list(map(int, input().split()))
for i in range(len(connected_info) - 1):
    first, second = connected_info[i], connected_info[i + 1]
    if find_parent(parent, first) != find_parent(parent, second):
        print('NO')
        exit(0)
print('YES')

