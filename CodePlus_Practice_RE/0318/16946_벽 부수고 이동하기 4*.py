'''
    그냥 모든 벽에 대해서 bfs는 시간 초과가 발생한다.

    플러드 필을 이용해 각각의 숫자로 칸을 채운다.
    이를 이용해 1을 뚫었을 때 채울 수 있는 모든 각각의 칸의 수를 더한다. 이 때 중복은 제거해야한다. (set)

'''

from collections import deque
from collections import defaultdict
from sys import stdin, stdout


input = stdin.readline
print = stdout.write

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_fill(x, y, count):

    q = deque()

    q.append((x, y))
    num = 1
    flood_fill[x][y] = count
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if flood_fill[nx][ny] == 0 and not arr[nx][ny]:
                q.append((nx, ny))
                flood_fill[nx][ny] = count
                #check[nx][ny] = True
                num += 1
    return num


result = [[0] * m for _ in range(n)]
flood_fill = [[0] * m for _ in range(n)]

fill_size = defaultdict(int)

count = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and flood_fill[i][j] == 0:
            fill_size[count] = bfs_fill(i, j, count)
            count += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            set_num = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                set_num.add(flood_fill[ni][nj])
            sm = 1
            for t in list(set_num):
                sm += fill_size[t]
                sm %= 10
            result[i][j] = sm

for row in result:
    print(''.join(map(str, row)) + '\n')