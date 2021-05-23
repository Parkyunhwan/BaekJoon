N = int(input())
arr = [[False] * 101 for _ in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
# 0 1 2 3 R U L D
dc = []

def init(): # 방향에 대한 규칙을 구해야하는 시뮬레이션 문제
    dc.append(0)
    for _ in range(11): # 세대
        for i in range(len(dc) - 1, -1, -1): # 방향

            dir = dc[i]
            dir = (dir + 1) % 4
            dc.append(dir)

init()

value = []
for _ in range(N):
    x, y, d, g = map(int, input().split())

    for idx in range(pow(2, g)):
        arr[x][y] = True
        dir = (dc[idx] + d) % 4
        x = x + dx[dir]
        y = y + dy[dir]
        arr[x][y] = True

count = 0
for i in range(100): # 101이 아니라 100이여만 인덱스에러가 나지 않는다.
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            count += 1

print(count)