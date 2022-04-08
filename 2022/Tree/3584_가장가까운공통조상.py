from collections import defaultdict
for _ in range(int(input())):
    N = int(input())
    graph = defaultdict(int)
    for _ in range(N - 1):
        parent, child = list(map(int, input().split()))
        graph[child] = parent

    a, b = list(map(int, input().split()))

    a_tree = []
    while graph[a]:
        a_tree.append(a)
        a = graph[a]
    a_tree.append(a)

    b_tree = []
    while graph[b]:
        b_tree.append(b)
        b = graph[b]
    b_tree.append(b)

    pre = 0
    r_atree = a_tree[::-1]
    r_btree = b_tree[::-1]
    for a, b in zip(r_atree, r_btree):
        if a == b:
            pre = a
        else:
            print(pre)
            break
    else:
        print(pre)