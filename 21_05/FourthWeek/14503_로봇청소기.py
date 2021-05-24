'''

    풀이 방법을 잘 설계에서 들어갔지만 '사소한 문제' 체크를 실수한 문제

    <문제가 되었던 부분>
    1. 방향 전환 시 dx, dy 값을 잘못 설정함.
    2. 증가하는 방향이 오른쪽 회전일 때 왼쪽회전을 어떻게 표현할 것인지에 대한 문제 (line 25)
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    # 현재 위치 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        count += 1

    flag = False
    for k in range(3, 3 * 5, 3):
        nd = (d + k) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if arr[nr][nc] == 0:
            r = nr
            c = nc
            d = nd
            flag = True
            break
    if flag:
        continue

    d = (d + 2) % 4
    r = r + dx[d]
    c = c + dy[d]

    if arr[r][c] == 1:
        break
    elif arr[r][c] == 2:
        d = (d + 2) % 4

print(count)
