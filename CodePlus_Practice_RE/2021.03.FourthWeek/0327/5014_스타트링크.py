from collections import deque
F, S, G, U, D =map(int, input().split())


dx = [U, -D]


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (F + 1)
    visited[start] = True
    while q:
        curr, count = q.popleft()

        if curr == G:
            return count
        for k in range(2):
            next = curr + dx[k]
            if 1 <= next <= F and not visited[next]:
                visited[next] = True
                q.append((next, count + 1))
    return -1


def solution():
    ret = bfs(S)
    if ret != -1:
        print(ret)
    else:
        print("use the stairs")



solution()