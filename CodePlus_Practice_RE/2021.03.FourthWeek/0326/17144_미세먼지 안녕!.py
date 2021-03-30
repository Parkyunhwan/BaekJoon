'''
    1시간 이상..걸림 (말그대로 막구현 함)
    https://rebas.kr/848 레바스 형님의 purify 메서드 체크 (문제 조건에 공기청정기가 2만큼 떨어져 있다는 것을 활용)

    공기청정기 나오는 부분이 '0'이라는 것도 포인트이다.
'''

from collections import deque


r, c, t = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

purifier = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            purifier.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def air_purifier():
    head, bottom = purifier[0], purifier[1]
    x, y = head[0], head[1]
    new_arr = [[-1] * c for _ in range(r)]
    for i in range(0, c - 1):
        if i == 0:
            new_arr[x][y + i + 1] = 0
        else:
            new_arr[x][y + i + 1] = arr[x][y + i]
    for i in range(x, 0, -1):
        new_arr[i - 1][c - 1] = arr[i][c - 1]
    for i in range(c - 1, 0, -1):
        new_arr[0][i - 1] = arr[0][i]
    for i in range(0, x - 1):
        new_arr[i + 1][0] = arr[i][0]

    x, y = bottom[0], bottom[1]

    for i in range(0, c - 1):
        if i == 0:
            new_arr[x][y + i + 1] = 0
        else:
            new_arr[x][y + i + 1] = arr[x][y + i]
    for i in range(x, r - 1):
        new_arr[i + 1][c - 1] = arr[i][c - 1]
    for i in range(c - 1, 0, -1):
        new_arr[r - 1][i - 1] = arr[r - 1][i]
    for i in range(r - 1, x + 1, -1):
        new_arr[i - 1][0] = arr[i][0]

    for i in range(r):
        for j in range(c):
            if new_arr[i][j] >= 0:
                if arr[i][j] == -1:
                    continue
                arr[i][j] = new_arr[i][j]


def spread():
    q = deque()
    spread_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        count = 0
        spread_value = arr[x][y] // 5
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or arr[nx][ny] == -1:
                continue
            spread_arr[nx][ny] += spread_value
            count += 1
        if count > 0:
            arr[x][y] -= spread_value * count

    # spread + arr
    for i in range(r):
        for j in range(c):
            arr[i][j] += spread_arr[i][j]

while t > 0:
    spread()
    air_purifier()
    t -= 1

sm = 0
for row in arr:
    sm += sum(row)
print(sm + 2)