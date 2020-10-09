#'.' 과 '#' 이 둘 다 front 혹은 back으로 들어가면
# 먼저 dist가 갱신된 경우 올바른 값을 출력하지 못할 수 있다.
# front부터 빼내고 있기 때문에 '.'이 front로 들어가야 최솟값을 찾을 수 있음
# 문을 여는 비용이 적은 녀석들을 먼저 탐색할 수 있도록 큐 대신 Deque를 사용해서 구현
from sys import stdin
from collections import deque
t = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def BFS(sx, sy):
    dist = [[-1]*(w+2) for _ in range(h+2)]
    q = deque()
    dist[sx][sy] = 0
    q.append((sx, sy))
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx+dx[k], ty+dy[k]
            if nx < 0 or nx >= h+2 or ny < 0 or ny >= w+2:
                continue
            if arr[nx][ny] == '*' or dist[nx][ny] != -1:
                continue
            elif arr[nx][ny] == '#':
                dist[nx][ny] = dist[tx][ty] + 1
                q.append((nx, ny))
            else:
                dist[nx][ny] = dist[tx][ty]
                q.appendleft((nx, ny))
    return dist


for _ in range(t):
    h, w = map(int, input().split())
    arr = ['.'*(w+2)]
    for _ in range(h):
        arr.append('.'+stdin.readline().strip()+'.')
    arr.append('.'*(w+2))
    #  시작 위치 찾기
    start = []
    for i in range(h+2):
        for j in range(w+2):
            if arr[i][j] == '$':
                # arr[i][j] = '.'  # 예외를 만들지 않기 위해 '.'으로 바꿔주는 것 중요
                start.append((i, j))

    move_arr = []
    for x, y in start:
        move_arr.append(BFS(x, y))
    dz = BFS(0, 0)
    mn = 987654321
    for i in range(h+2):
        for j in range(w+2):
            if arr[i][j] == '*':
                continue
            sm = dz[i][j]
            for t in range(len(move_arr)):
                sm += move_arr[t][i][j]
            if arr[i][j] == '#':
                sm -= len(move_arr)
            mn = min(mn, sm)
    print(mn)