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

dx0 = [-1, -1, 0, 1, 1, 0]
dy0 = [-1, 0, 1, 0, -1, -1]
dx1 = [-1, -1, 0, 1, 1, 0]
dy1 = [0, 1, 1, 1, 0, -1]
arr = []
for _ in range(H):
    arr.append([0] + list(map(int, input().split())) + [0])
arr = [[0] * (W + 2)] + arr + [[0] * (W + 2)]

def bfs(x, y):
    count = 0
    q = deque()
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for k in range(6):
            if x % 2 == 0:
                nx, ny = x + dx0[k], y + dy0[k]
            else:
                nx, ny = x + dx1[k], y + dy1[k]
            if nx < 0 or ny < 0 or nx >= H + 2 or ny >= W + 2:
                continue
            if arr[nx][ny] == 1:
                count += 1
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])
    return count
print(bfs(0, 0))