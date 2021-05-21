# 사이클이라면 (그래프 간선 + 1) -> + 1 은 temp 사용한 것
# 사이클이 아니라면 그 그래프의 간선의 갯수
from collections import defaultdict

def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x == y:
        return False # cycle
    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x
    return True

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]



def solution(before, after):
    length = len(before)

    parent = defaultdict(str)
    count = 0
    for i in range(length):
        if before[i] not in parent:
            parent[before[i]] = before[i]
        if after[i] not in parent:
            parent[after[i]] = after[i]
        if before[i] == after[i]:
            continue
        if union_parent(parent, before[i], after[i]):
            count += 1
        else:
            count += 2

    return count