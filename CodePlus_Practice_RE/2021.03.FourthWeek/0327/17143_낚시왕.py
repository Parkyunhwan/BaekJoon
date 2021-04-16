'''
   Review 완료

   -> 너무 아쉽게도 반복되는 구간의 계산 횟수를 줄이지 못했다. https://rebas.kr/847

'''
import sys
input = sys.stdin.readline
r, c, m = map(int, input().split())

if m == 0:
    print(0)
    exit(0)
shark_info = [list(map(int, input().split())) for _ in range(m)]


arr = [[[0] * 3 for _ in range(c + 2)] for _ in range(r + 2)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

for shark in shark_info:
    a, b, t, d, e = shark
    # c, d, e -> 속력, 이동방향, 사이즈
    arr[a][b][0] = t
    arr[a][b][1] = d
    arr[a][b][2] = e

man = 0
score = 0
while man <= c:
    man += 1

    # 낚시왕의 낚시 타임
    for i in range(1, r + 1):
        if arr[i][man][1] > 0:
            score += arr[i][man][2]
            arr[i][man] = [0, 0, 0]
            break


    # 상어 이동
    new_arr = [[[0] * 3 for _ in range(c + 2)] for _ in range(r + 2)]

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if arr[i][j][1] > 0:

                speed, direction, size = arr[i][j]
                move_num = speed

                if direction < 3:

                    ns, nd, ni = move_num % ((r - 1) * 2), direction, i

                    for _ in range(ns):
                        if ni == 1 and nd == 1:
                            nd = 2
                        if ni == r and nd == 2:
                            nd = 1
                        ni += dx[nd]
                    if new_arr[ni][j][2] < size:
                        new_arr[ni][j] = [speed, nd, size]
                else:
                    ns, nd, nj = move_num % ((c - 1)*2), direction, j

                    for _ in range(ns):
                        if nj == 1 and nd == 4:
                            nd = 3
                        if nj == c and nd == 3:
                            nd = 4
                        nj += dy[nd]
                    if new_arr[i][nj][2] < size:
                        new_arr[i][nj] = [speed, nd, size]

    arr = new_arr[:]

print(score)

