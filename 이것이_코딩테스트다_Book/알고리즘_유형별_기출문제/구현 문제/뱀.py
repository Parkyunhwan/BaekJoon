# 1회차 -> 맞음
from collections import deque
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apple = [list(map(int, input().split())) for _ in range(k)]

l = int(input()) # 방향 변환 횟수
snake = [list(input().split()) for _ in range(l)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
map = [[0]*n for _ in range(n)]
# 1. 맵에 사과 설치
for a in apple:
    i, j = a
    map[i-1][j-1] = 1 # apple 은 1

time = 0
nx, ny, dir = 0, 0, 0 # 뱀의 초기 위치와 방향 설정
tx, ty = 0, 0
snakeq = deque()
snakeq.append((0, 0))
map[0][0] = 2
while True:
    if len(snake) > 0:
        rotation_time, next_dir = snake.pop(0)
    else:
        rotation_time = int(1e9)
    for i in range(time, int(rotation_time)):
        nx, ny = nx + dx[dir], ny + dy[dir]
        time += 1
        if nx < 0 or nx >= n or ny < 0 or ny >= n or map[nx][ny] == 2:
            #  종료
            print(time)
            exit(0)
        else:
            snakeq.appendleft((nx, ny))
            if map[nx][ny] == 0:
                tx, ty = snakeq.pop()
                map[tx][ty] = 0
            map[nx][ny] = 2
    # 방향 전환
    if next_dir == 'D':
        dir = (dir+1)%4
    else:
        dir = (dir+3)%4

