'''
    https://rebas.kr/779

'''

from collections import deque
m, n = map(int, input().split())


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

wall = []
for i in range(n):
    row = list(map(int, input().split()))
    wall_row = []
    for j in range(m):
        li = list(bin(row[j])[2:])
        while len(li) != 4:
            li = ['0'] + li
        wall_row.append(li)
    wall.append(wall_row)


def bfs(sx, sy, number):
    size = 0
    q = deque()
    q.append((sx, sy))

    castle[sx][sy] = number
    while q:
        x, y = q.popleft()
        size += 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or castle[nx][ny] != 0:
                continue

            if wall[x][y][k] == '1':  # 벽이면 넘어가~
                continue
            castle[nx][ny] = number
            q.append((nx, ny))

    return size



castle = [[0] * m for _ in range(n)]

result = [0, 0, 0]
color = 1


castle_size = []
for i in range(n):
    for j in range(m):
        if castle[i][j] == 0:
            size = bfs(i, j, color)
            color += 1
            castle_size.append(size)

result[0] = color - 1
result[1] = max(castle_size)

max_size = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if ni < 0 or nj < 0 or ni >= n or nj >= m or visited[ni][nj]:
                continue
            visited[ni][nj] = True

            if castle[i][j] != castle[ni][nj]:
                size = castle_size[castle[i][j] - 1] + castle_size[castle[ni][nj] - 1]
                max_size = max(max_size, size)

result[2] = max_size
for val in result:
    print(val)
