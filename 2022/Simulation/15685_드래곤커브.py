import sys
input = sys.stdin.readline
dir_hist = []
def init_dir():
    dir_hist.append(0) # 방향 0으로 시작
    for _ in range(11):
        for i in range(len(dir_hist) - 1, -1, -1):
            curr_dir = dir_hist[i]
            next_dir = (curr_dir + 1) % 4
            dir_hist.append(next_dir)

N = int(input())
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# -> 문제를 내 기준으로 바꿔서 하려면 아래 dx, dy를 사용해야한다.
# 문제에서 친절히 x좌표가 증가하는 방향이라고 했고 x, y가 순서대로 나오는 것도 알려줬다.
dx = [1,0,-1,0]
dy = [0,-1,0,1]
visited = [[False] * 101 for _ in range(101)]
init_dir()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    for idx in range(pow(2, g)):
        visited[x][y] = True
        dir = (dir_hist[idx] + d) % 4
        x, y = x + dx[dir], y + dy[dir]
        visited[x][y] = True

count = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
            count += 1

print(count)