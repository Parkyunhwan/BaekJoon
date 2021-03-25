'''
    풀이시간 : 30분 (완료)

    첫트 틀린 이유 : 방문된 위치도 더 작은 거울 횟수에 의해 갱신될 수 있다.
                  그러나, 현재 위치의 거울 횟수를 갱신할 수 없다고 그 다음 위치의 거울 횟수를 갱신할 수 없는 것은 아니다.
'''

from collections import deque
import sys
w, h = map(int, input().split())

arr = [list(input()) for _ in range(h)]

laser = []
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            laser.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mirror = [[sys.maxsize] * w for _ in range(h)]


def bfs(x, y):
    q = deque()

    q.append((x, y))
    mirror[x][y] = -1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            while 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*':
                if mirror[nx][ny] > mirror[x][y] + 1:
                    mirror[nx][ny] = mirror[x][y] + 1
                    q.append((nx, ny))
                nx, ny = nx + dx[k], ny + dy[k]


laser_start = laser[0]
laser_end = laser[1]
bfs(laser_start[0], laser_start[1])

print(mirror[laser_end[0]][laser_end[1]])