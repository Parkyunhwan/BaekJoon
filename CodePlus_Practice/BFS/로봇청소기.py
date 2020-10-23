# --> 틀린 코드... 지금 위치에서 가장 가까운 거리를 선택한다고 해도
# --> 전체 거리에서 가장 가까운 거리를 보장하지 않는다.. ( 가장 중요!! )
# --> 즉, 각자의 최적값의 합이 전체 최적값을 보장하지 않는다.
# 1. 로봇의 위치에서 쓰레기의 위치를 기록한다.
# 2. 로봇으로부터 쓰레기의 거리를 구한다.
# 3. 쓰레기 간 거리를 구한다.
# 4. 순열로 가능한 모든 경로를 구하고 거리를 다 더해서 최솟값을 출력한다.

# 3회차 시 -> 성공
from collections import deque
from itertools import permutations
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    dist = [[-1]*w for _ in range(h)]
    dist[sx][sy] = 0
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if nx < 0 or nx >= h or ny < 0 or ny >= w or arr[nx][ny] == 'x' or dist[nx][ny] != -1:
                continue
            else:
                dist[nx][ny] = dist[tx][ty] + 1
                q.append((nx, ny))
    return dist


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(input()) for _ in range(h)]

    # 로봇 위치와 쓰레기 위치 파악
    robot = []
    trash = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                robot.append((i, j))
            elif arr[i][j] == '*':
                trash.append((i, j))

    r2t = bfs(robot[0][0], robot[0][1])

    flag = False
    for t in trash:
        if r2t[t[0]][t[1]] == -1:
            print(-1)
            flag = True
            break
    if flag:
        continue

    t2t = []
    for t in trash:
        t2t.append(bfs(t[0], t[1]))

    mn = int(1e9)
    li = [x for x in range(len(trash))]
    for per in list(permutations(li, len(trash))):
        first = per[0]
        x, y = trash[first][0], trash[first][1]
        distance = r2t[x][y]
        prev = first
        for i in range(1, len(per)):
            index = per[i]
            x, y = trash[index][0], trash[index][1]
            distance += t2t[prev][x][y]
            prev = index
        mn = min(mn, distance)

    print(mn)

#  https://chldkato.tistory.com/66
from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(x, y):
    q = deque()
    c = [[0]*w for _ in range(h)]
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] != 'x' and not c[nx][ny]:
                    c[nx][ny] = c[x][y] + 1
                    q.append([nx, ny])
    return c

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    a, d = [], []
    for i in range(h):
        row = list(input().strip())
        a.append(row)
        for j, k in enumerate(row):
            if k == 'o':
                sx, sy = i, j
            elif k == '*':
                d.append([i, j])

    r2d, flag = [], 0
    c = bfs(sx, sy)    #   로봇으로 부터 모든 위치를 구함

    for i, j in d:   # 모든 쓰레기의 위치
        if not c[i][j]:  # check가 안되있다면 접근 불가능 한 쓰레기가 있음
            flag = 1
            break
        r2d.append(c[i][j]-1)
    if flag:
        print(-1)
        continue

    d2d = [[0]*len(d) for _ in range(len(d))]  # 쓰레기 사이의 거리를 기록하기 위함
    for i in range(len(d) - 1):
        c = bfs(d[i][0], d[i][1])  # i 번째 쓰레기로 부터 모든 거리 계산
        for j in range(i+1, len(d)):
            d2d[i][j] = c[d[j][0]][d[j][1]]  # j 번째 쓰레기 까지의 거리
            d2d[j][i] = d2d[i][j]  # j to i 는 i to j랑 같다.

    p = list(permutations([i for i in range(len(d2d))])) # 쓰레기 끼리 순열을 모두 구함
    ans = sys.maxsize
    for i in p: #  p에는 길이가 len(d2d)인 순열만 존재한다.
        #  처음은 로봇에서 쓰레기 거리
        dist = 0
        dist += r2d[i[0]]
        nfrom = i[0]  # 로봇에서 쓰레기로 위치 바꿈
        for j in range(1, len(i)):  # 쓰레기에서 다음 쓰레기까지
            nto = i[j]  # 다음 쓰레기
            dist += d2d[nfrom][nto]
            nfrom = nto
        ans = min(ans, dist)
    print(ans)


# --> 틀린 코드... 지금 위치에서 가장 가까운 거리를 선택한다고 해도
# --> 전체 거리에서 가장 가까운 거리를 보장하지 않는다..
#  처음 보기엔 전형적인 BFS 문제이다.
#  특이한 점은 로봇이 같은 칸을 여러번 방문할 수 있다는 점이다.
#  왔던길을 다시 되돌아가도 된다..
#  *..O..* 이런 경우를 위해서 인것 같다.
# 로봇에서 쓰레기1로 보물1에서 쓰레기2로 보물2에서 쓰레기3으로 (쓰레기가 없을때까지 반복
# 쓰레기의 위치를 넣어둔 후 쓰레기를 찾으면 그 위치부터 다시 탐색을 시작한다. 모든 쓰레기 찾을때까지 반
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def BFS(x, y):
    check = [[False]*w for _ in range(h)]
    q = deque()
    q.append((x, y, 0))
    while q:
        tx, ty, count = q.popleft()
        for k in range(4):
            nx, ny = tx+dx[k], ty+dy[k]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if arr[nx][ny] == 'x' or check[nx][ny]:
                continue
            elif arr[nx][ny] == '*':
                return nx, ny, count+1
            else:
                check[nx][ny] = True
                q.append((nx, ny, count+1))
    return -1, -1, -1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    result = 0
    arr = [list(input()) for _ in range(h)]
    robot = deque()
    trash = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '.' or arr[i][j] == 'x':
                continue
            elif arr[i][j] == '*':
                trash += 1
            else:
                arr[i][j] = '.'
                robot.append((i, j))

    find_trash = 0
    while robot:
        rx, ry = robot.popleft()
        nrx, nry, co = BFS(rx, ry)
        if nrx == -1 and nry == -1 and co == -1:
            break
        find_trash += 1
        arr[nrx][nry] = '.'
        result += co
        robot.append((nrx, nry))

    print(result if find_trash == trash else -1)