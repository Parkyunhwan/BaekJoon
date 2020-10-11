from collections import deque
n, m = map(int, input().split())
sx, sy, sdir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
q.append((sx, sy, sdir))
arr[sx][sy] = 1
count = 1
dx = (-1, 0, 1, 0)  # 북 동 남 서
dy = (0, 1, 0, -1)
while q:
    x, y, dir = q.popleft()
    for _ in range(4):
        if dir + 1 == 4:
            dir = 0
        else:
            dir += 1

        nx, ny = x + dx[dir], y + dy[dir]
        print(nx, ny)
        #맵의 가장자리는 항상 바다이기 때문에 필요가 없는 조건이다.
        #if nx < 0 or nx >= n or ny < 0 or ny >= m:
        #    continue
        if arr[nx][ny]:
            continue
        arr[nx][ny] = 1
        count += 1
        q.append((nx, ny, dir))
print(count)