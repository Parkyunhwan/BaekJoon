'''

틀린 이유는 바이러스 놓는 곳을 0으로 시작했기 때문이다.

해당 반례 처럼 바이러스를 놓자마자 빈칸이 없는 경우를 체크하지 못했다.
5 2
1 1 1 1 1
1 1 2 1 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1

바이러스를 0으로 놓고 시작했을 때 생기는 또다른 문제는 바이러스가 서로 인접하게 시작할 때
큐에는 이미 바이러스가 들어가 있는데 인접한 바이러스에 의해 현재 바이러스 값이 0이아닌값으로 변화하게 된다.

결론적으로 0으로 시작하는 것은 위험하며 1로 시작하거나 count를 큐에 넣는 것을 추천한다.
'''

from itertools import combinations
from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


virus_possible = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_possible.append((i, j))
            arr[i][j] = 0
        elif arr[i][j] == 1:
            arr[i][j] = -1
iter_num = [i for i in range(0, len(virus_possible))]
comb = list(combinations(iter_num, M))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(com):
    q = deque()
    visited = [row[:] for row in arr]

    for i in com:
        x, y = virus_possible[i]
        q.append((x, y))
        visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == -1:
                continue
            if visited[nx][ny] != 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    max_value = 0
    for row in visited:
        if 0 in row:
            return -1
        max_value = max(max_value, max(row))
    return max_value - 1


answer = 1e9
for com in comb:
    ret = bfs(com)
    if ret != -1:
        answer = min(answer, ret)

if answer == 1e9:
    print(-1)
else:
    print(answer)

