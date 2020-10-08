# https://rebas.kr/768
from collections import deque


def bfs():
    while q:
        d = q.popleft()
        if d == 123456789:  # 문자열을 통한 비교 ㄷㄷ
            print(dist[d])
            return
        s = str(d)
        k = s.find('9')  # 9의 index 탐색
        x, y = k // 3, k % 3
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 0~3
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            nk = nx*3 + ny  # 바꿀 위치
            ns = list(s)
            ns[k], ns[nk] = ns[nk], ns[k]  # 리스트를 통한 swap 식
            nd = int(''.join(ns))  # 다시 문자열로..
            if not dist.get(nd):  # 방문 여부 확인
                dist[nd] = dist[d] + 1  # 이전 위치에서 + 1
                q.append(nd)
    print(-1)


q = deque()
dist = dict()
a = [list(map(int, input().split())) for _ in range(3)]
m = 0
for i in range(3):
    for j in range(3):
        n = a[i][j]
        if not n:  # 0이면 9로
            n = 9
        m = m*10 + n  # 3x3배열로 현재 상태를 저장하지 않고 문자열 하나로 저장하기 위해
q.append(m)
dist[m] = 0  # 문자열 통한 방문 여부 판단과 count 기록
bfs()


#  ______시간초과, 메모리초과의 내코드..________
#  메모리가 작다는 것을 알았지만 배열에 넣어서 저장하려 했고 실패했다.
#  dict에 대한 이용과 문자열을 통해서 방문 판단을 할수 있다는 것도 알수 있었다.

# from collections import deque
# arr = [list(map(int, input().split())) for _ in range(3)]
# x = y = 0
# for i in range(3):
#     for j in range(3):
#         if arr[i][j] == 0:
#             x = i; y = j
#             break
#
# q = deque()
# q.append((arr, x, y, 0))
#
#
# while q:
#     a, i, j, count = q.popleft()
#     flag = True
#     for ti in range(3):
#         for tj in range(3):
#             if a[ti][tj] != (ti*3 + tj+1) % 9:
#                 flag = False
#         if not flag:
#             break
#     if flag:
#         print(count)
#         break
#
#     for k in range(4):
#         back = [x[:] for x in a]
#         if k == 0:  # left
#             if j == 0:
#                 continue
#             else:
#                 tmp = back[i][j]
#                 back[i][j] = back[i][j - 1]
#                 back[i][j - 1] = tmp
#                 q.append((back, i, j - 1, count + 1))
#
#         elif k == 1:  # right
#             if j == 2:
#                 continue
#             else:
#                 tmp = back[i][j]
#                 back[i][j] = back[i][j+1]
#                 back[i][j+1] = tmp
#                 q.append((back, i, j + 1, count + 1))
#
#         elif k == 2:  # Up
#             if i == 0:
#                 continue
#             else:
#                 tmp = back[i][j]
#                 back[i][j] = back[i-1][j]
#                 back[i-1][j] = tmp
#                 q.append((back, i - 1, j, count + 1))
#
#         elif k == 3:  # Down
#             if i == 2:
#                 continue
#             else:
#                 tmp = back[i][j]
#                 back[i][j] = back[i + 1][j]
#                 back[i + 1][j] = tmp
#                 q.append((back, i + 1, j, count + 1))

#  모든 경우의 수를 표현할 수 있어야한다. 즉 -> 123456789의 순서로 방문을 표시해야한다.
#  왼오위아래

#  두번째 시도 성공..!
from collections import deque


def BFS(sx, sy, ch):
    q = deque()
    q.append((sx, sy, ch, 0))

    while q:
        tx, ty, ch, count = q.popleft()
        if "123456789" == ch:
            return count
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = tx + dx, ty + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                a = list(ch)
                tmp = a[tx*3 + ty]
                a[tx*3 + ty] = a[nx*3 + ny]
                a[nx*3 + ny] = tmp
                c = ''.join(a)
                if not dict_check.get(c):
                    dict_check[c] = 1
                    q.append((nx, ny, c, count+1))
    return -1


arr = [input().split() for _ in range(3)]
check = []
start_x, start_y = 0, 0
dict_check = dict()
for i in range(3):
    for j in range(3):
        if arr[i][j] == '0':
            arr[i][j] = '9'
            start_x = i
            start_y = j
        check.append(arr[i][j])
check = ''.join(check)
dict_check[check] = 1
print(BFS(start_x, start_y, check))
