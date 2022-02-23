V, E = map(int, input().split())

root = [i for i in range(0, V + 1)]
cost_sum = 0

def find(x):
    global root
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x > y:
        root[x] = y
    else:
        root[y] = x

info = []
for _ in range(E):
    info.append(list(map(int, input().split())))


info.sort(key=lambda x:x[2])
for val in info:
    v1, v2, cost = val
    v1_root = find(v1)
    v2_root = find(v2)
    if v1_root == v2_root:
        continue
    else:
        union(v1, v2)
        cost_sum += cost

