#  그냥 방향 꺽을 때 거울을 썻다 라고 표시..? (우선순위큐사용)
#  맞긴 맞는데 우선순위큐로 풀 수 없다. 방문 check에서 꼬임
#  https://yabmoons.tistory.com/125 (나와 가장 비슷한 풀이) 갱신이 안되면 큐에 넣지 않는 것이 Check배열이라고 볼 수 있다.

from sys import stdin
from collections import deque
input = stdin.readline

w, h = map(int, input().split())
a = [list(input().strip()) for _ in range(h)]
dist = [[0]*w for _ in range(h)]
q = deque()
ex, ey = -1, 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dy, y+dy
            while 0 <= nx < h and 0 <= ny < w and a[nx][ny] != '*':
                if not dist[nx][ny]:
                    dist[nx][ny] = dist[nx][ny] + 1
                    q.append((nx, ny))
                nx, ny = nx+dx, ny+dy

for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if ex == -1:
                ex, ey = i, j
            else:
                q.append((i, j))

bfs()
print(dist[ex][ey]-1)