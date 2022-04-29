'''
    이 문제는 벽으로 둘러쌓여있는 빈공간을 체크하지 않도록 하는 문제이다.
    그렇게 하기 위해서는 벽 주변을 체크하면 안된다.
    벽 외부를 만들어서라도 벽의 주변을 하나씩 모두 체크해나가야한다. (벽 내부로는 들어갈 수 없음)
    핵심
    * 외부 공간을 만들 것
    * 빈 공간에서부터 그래프 탐색으로 벽 주변을 모두 탐색할 것
    * 문제에 있는 육각형이동 예외를 체크 할 것
'''
from collections import deque
W, H = map(int, input().split())

arr = []
for _ in range(H):
    arr.append([0] + list(map(int, input().split())) + [0])
arr = [[0] * (W + 2)] + arr + [[0] * (W + 2)]

dx_odd = [-1, 0, 1, -1, 1, 0]
dy_odd = [-1, -1, -1, 0, 0, 1]

dx_even = [-1, -1, 0, 1, 1, 0]
dy_even = [0, 1, 1, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    count = 0
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        if x % 2 == 1:
            dx = dx_even
            dy = dy_even
        else:
            dx = dx_odd
            dy = dy_odd

        for k in range(6):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= (H + 2) or ny >= (W + 2):
                continue
            if visited[nx][ny]:
                continue

            if arr[nx][ny] == 1:
                count += 1
            if arr[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))

    return count

visited = [[False] * (W + 2) for _ in range(H + 2)]
cnt = bfs()

print(cnt)