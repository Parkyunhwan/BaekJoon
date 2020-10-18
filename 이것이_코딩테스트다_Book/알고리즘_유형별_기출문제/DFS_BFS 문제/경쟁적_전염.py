# 1회차 -> 성공
# 아쉽게도 한번에 맞추지 못했다. 오류는 문제를 완전히 이해하지 않은 것에서 나왔다.
# 시간 전에 모든 바이러스가 시험관에 전염되었을 때 해당 위치의 값을 출력해줘야한다.
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    q = deque()
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                tmp.append((arr[i][j], i, j))
    tmp.sort()
    for t in tmp:
        q.append((t[1], t[2], 0))
    while q:
        x, y, time = q.popleft()
        if time == S:
            if arr[X-1][Y-1]:
                print(arr[X-1][Y-1])
            else:
                print(0)
            exit(0)
            return
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
                continue
            else:
                arr[nx][ny] = arr[x][y]
                q.append((nx, ny, time + 1))
    print(arr[X-1][Y-1])


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

BFS()