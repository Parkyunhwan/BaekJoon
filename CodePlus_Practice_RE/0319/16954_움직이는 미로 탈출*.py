'''

    모든 방향으로 탐색을 진행해야 한다. (확실하지 않다면 모든 방향으로 하자).....(이것 땜에 틀림)

    나는 전체 상황을 저장한 후 비교해서 구했다. (메모리 사용)

    아래 블로그 처럼 시간 t를 이용해 해당 row를 검사하는 것이 더 좋은 방법이다.
    https://100100e.tistory.com/246
    https://dirmathfl.tistory.com/185
'''
from collections import deque
arr = [list(input()) for _ in range(8)]

dx = [-1, -1, -1, 0, 0, 0, -1, 0, 1]
dy = [-1, 0, 1, -1, 1, 0, 1, 1, 1]

arr_situation = [[['.'] * 9 for _ in range(8)] for _ in range(8)]
visited = [[[False] * 9 for _ in range(8)] for _ in range(8)]
for k in range(9):
    for i in range(8):
        if i + k >= 8:
            break
        for j in range(8):
            arr_situation[i + k][j][k] = arr[i][j]
#
# for k in range(9):
#     print(k)
#     for i in range(8):
#         for j in range(8):
#             print(arr_situation[i][j][k], end=' ')
#         print()
#     print()

def bfs():
    q = deque()
    q.append((7, 0, 0))

    while q:
        x, y, num = q.popleft()
        if arr_situation[x][y][num] == '#': # 벽이 덮쳐 버린 경
            continue
        if x == 0 and y == 7:
            return 1

        for k in range(9):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx > 7 or ny > 7:
                continue
            if visited[nx][ny][num]:
                continue
            if arr_situation[nx][ny][num] != '#':
                if num == 8:
                    visited[nx][ny][8] = True
                    q.append((nx, ny, num))
                else:
                    visited[nx][ny][num] = True
                    q.append((nx, ny, num + 1))
    return 0
print(bfs())