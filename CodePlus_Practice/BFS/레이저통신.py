#  그냥 방향 꺽을 때 거울을 썻다 라고 표시..? (우선순위큐사용)
#  맞긴 맞는데 우선순위큐로 풀 수 없다. 방문 check에서 꼬임
#  https://yabmoons.tistory.com/125 (나와 가장 비슷한 풀이) 갱신이 안되면 큐에 넣지 않는 것이 Check 배열이라고 볼 수 있다.

# 몇번 꺽었는가가 가장 중요한 포인트이다. 몇번 움직였는지는 중요하지 않다.
# 그러므로 적게 꺽은 수일 수록 큐의 앞에 위치 해야만 한다. 몇번 움직였는지는 전혀 중요치 않다.

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