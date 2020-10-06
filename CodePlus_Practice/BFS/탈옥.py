#  죄수가 두 명인 문제
#  기존과는 다른 방식으로 생각해야함
#  두 명이 같이 움직이는 것을 어떻게 표현할까? -> 일단 rebas님은 하나씩 BFS를 수행함
#  한 명이 탈출했을 때 남아 있는 다른 한명은 어떻게 진행할 것인가? -> 따로 진행
from sys import stdin
from collections import deque

n = int(input())

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def BFS(x, y):
    q = deque()
    dist = [[-1] * (w + 2) for _ in range(h + 2)]
    q.append((x, y))
    dist[x][y] = 0
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if nx < 0 or nx > h + 1 or ny < 0 or ny > w + 1:
                continue
            if dist[nx][ny] >= 0 or arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '.':
                dist[nx][ny] = dist[tx][ty]
                q.append((nx, ny))
            elif arr[nx][ny] == '#':
                dist[nx][ny] = dist[tx][ty] + 1
                q.append((nx, ny))
    return dist


for _ in range(n):
    h, w = map(int, input().split())
    arr = ['.'*(w + 2)]
    for _ in range(h):
        arr.append(list('.' + stdin.readline().strip() + '.'))
    arr.append(list('.' * (w + 2)))
    prisoner = deque()
    pris = 0
    for i in range(h + 2):
        for j in range(w + 2):
            if arr[i][j] == '$':
                arr[i][j] = '.'
                prisoner.append((i, j))
    fx, fy = prisoner.popleft()
    df = BFS(fx, fy)
    sx, sy = prisoner.popleft()
    ds = BFS(sx, sy)
    dz = BFS(0, 0)
    ans = 1e9
    for i in range(h+2):
        for j in range(w+2):
            if arr[i][j] == '*':
                continue
            k = df[i][j] + ds[i][j] + dz[i][j]
            if arr[i][j] == '#':
                k -= 2
            ans = min(ans, k)
    print(ans)
