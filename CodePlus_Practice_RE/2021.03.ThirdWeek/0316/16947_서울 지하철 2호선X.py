'''
    풀이에 필요한 두 가지 생각

    순환역에 속해있는 역을 찾는다. (DFS)

    순환역에 속해있지 않은 역에서 순환역에 속한 역까지 최소 거리를 구한다. (BFS)

'''
import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 필수...only 백준
n = int(input())


graph = defaultdict(list)
visited = [False] * (n + 1)
cycle_pos = [False] * (n + 1)
result = [0] * (n + 1)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(curr, start_station, num):
    if curr == start_station and num >= 2:  # 2인 이유는 2개의 정점으로 순환을 만들지 못하기 때문 (3개 이상)
        cycle_pos[start_station] = True
        return
    visited[curr] = True
    for next in graph[curr]:
        if not visited[next]:
            dfs(next, start_station, num + 1)
        else:
            if next == start_station and num >= 2:
                dfs(next, start_station, num)
    if cycle_pos[start_station]:
        return True


def bfs(start, num):
    q = deque()
    visited[start] = True
    q.append((start, num))
    while q:

        curr, num = q.popleft()

        if cycle_pos[curr]:
            return num
        for ne in graph[curr]:
            if not visited[ne]:
                visited[curr] = True
                q.append((ne, num + 1))


for i in range(1, n + 1):
    visited_save = visited[:]
    dfs(i, i, 0)
    visited = visited_save[:]

for i in range(1, n + 1):
    if not cycle_pos[i]:
        visited_save = visited[:]
        result[i] = bfs(i, 0)
        visited = visited_save[:]
    else:
        result[i] = 0

for i in range(1, n + 1):
    print(result[i], end=' ')
