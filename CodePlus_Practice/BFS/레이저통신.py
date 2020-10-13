#  그냥 방향 꺽을 때 거울을 썻다 라고 표시..? (우선순위큐사용)
#  맞긴 맞는데 우선순위큐로 풀 수 없다. 방문 check에서 꼬임
#  https://yabmoons.tistory.com/125 (나와 가장 비슷한 풀이) 갱신이 안되면 큐에 넣지 않는 것이 Check 배열이라고 볼 수 있다.

# 몇번 꺽었는가가 가장 중요한 포인트이다. 몇번 움직였는지는 중요하지 않다.
# 그러므로 적게 꺽은 수일 수록 큐의 앞에 위치 해야만 한다. 몇번 움직였는지는 전혀 중요치 않다.
#  어떤 것의 최솟값을 구할 것인가??? -> 설치해야하는 거울의 최솟값 -> dist의 원소
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def BFS(sx, sy):
        q = deque()
        q.append((sx, sy))
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                # 다른 BFS와 다른 부분
                while 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*':
                    if not dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + 1  # x, y 의 값에 1을 더한 것이다.
                        q.append((nx, ny))
                    nx, ny = nx + dx[k], ny + dy[k]



w, h =map(int, input().split())
arr = [list(input()) for _ in range(h)]
dist = [[0] * w for _ in range(h)]
#  C의 위치 확인
c_pos = []
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            c_pos.append((i, j))

BFS(c_pos[0][0], c_pos[0][1])
print(dist[c_pos[1][0]][c_pos[1][1]]-1)