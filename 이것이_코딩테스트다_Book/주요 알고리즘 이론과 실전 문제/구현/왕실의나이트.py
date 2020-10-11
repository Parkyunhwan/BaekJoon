# 방향의 경우의 수가 8개인 문제였다. 방향이 이보다 많다면 아래 처럼 풀어야 할 것 같다.
# 하지만 방향이 적다면 그냥
# steps = [(-2,-1), (-1,-2), ... (-2, 1)] 처럼 8개를 지정해주는 것이 더 쉽다.
# dx, dy 처럼 행과 열을 나눌 수도 있고 steps처럼 행과 열을 같이 둘수 도 있다.

pos = list(input())
start_x = ord(pos[0]) - ord('a')
start_y = int(pos[1]) - 1

move_direction1 = ("L", "R", "U", "D")  # L, R, U, D
move_direction2 = ("U", "D")
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
count = 0
for i in range(len(move_direction1)):
    tx, ty = start_x + dx[i]*2, start_y + dy[i]*2
    if tx < 0 or tx >= 8 or ty < 0 or ty >= 8:
        continue
    for j in range(len(move_direction2)):
        if i < 2:
            nx, ny = tx + dx[j+2], ty + dy[j+2]
        else:
            nx, ny = tx + dx[j], ty + dy[j]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        count += 1
print(count)
