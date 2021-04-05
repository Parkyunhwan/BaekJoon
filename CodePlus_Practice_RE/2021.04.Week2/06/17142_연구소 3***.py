'''
https://rebas.kr/846
rebas님으 풀이방식 check

맵과 dist 배열을 따로 둬서
이동횟수와 제약조건을 분리했다.

또한 infect와 빈 공간 갯수를 이용해
모두 퍼뜨릴 수 있는지도 좀 더 빠르게 체크할 수 있었다.
'''

from itertools import combinations
from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

virus_possible = []
nothing_place = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_possible.append((i, j))
        elif arr[i][j] == 0:
            nothing_place += 1
it = [x for x in range(len(virus_possible))]
comb = list(combinations(it, M))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(combi):
    visited = [[-1] * N for _ in range(N)]
    time = 0
    infect = 0
    q = deque()
    for val in combi:
        x, y = virus_possible[val]
        q.append((x, y))
        visited[x][y] = 0
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] == 1 or visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            if arr[nx][ny] == 0:
                infect += 1
                time = visited[nx][ny]

    if nothing_place == infect:
        return time
    else:
        return -1


result = 1e9
for com in comb:
    ret = bfs(com)
    if ret != -1:
        result = min(ret, result)

if result == 1e9:
    print(-1)
    exit(0)
print(result)
