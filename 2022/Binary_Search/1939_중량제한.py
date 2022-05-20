import sys
from collections import defaultdict, deque
N, M = map(int, input().split())
input = sys.stdin.readline
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
x, y = map(int, input().split())

def isPossible(possible_weight):
    visited = [False] * (N + 1)
    q = deque()
    q.append(x)
    while q:
        curr = q.popleft()
        if curr == y:
            return True # 연결 가능함

        for v_next, v_weight in graph[curr]:
            if v_weight < possible_weight:
                continue
            if visited[v_next]:
                continue
            visited[v_next] = True
            q.append(v_next)

    return False # 연결 불가능함


visited = [False] * (N + 1)
left_value, right_value = 0, pow(10, 9)
while True:
    if left_value > right_value:
        break
    mid = (left_value + right_value) // 2

    if isPossible(mid):
        left_value = mid + 1
    else:
        right_value = mid - 1

print(right_value)