from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

arr = [list(map(int, list(input().strip()))) for _ in range(n)]

# vistied[x][y][skill] 체크 배열
visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, k):
    q = deque()
    # x, y
    # k : 남은 스킬 횟수
    # 0 : 낮, 1 : 밤
    # dist : 현재 거
    q.append((x, y, k, 0, 1))
    visited[x][y][k] = True
    while q:
        x, y, skill, statue, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 1: # 벽일 때
                if skill > 0 and statue == 0 and not visited[nx][ny][skill - 1]: # 낮이므로 벽부수고 진행
                    visited[nx][ny][skill - 1] = True
                    q.append((nx, ny, skill - 1, 1, dist + 1))
                # visited[nx][ny][skill - 1] 을 검사해야만 한다. visited[nx][ny][skill]을 검사하는 것은 의미가 없다.
                elif skill > 0 and statue == 1 and not visited[nx][ny][skill - 1]: # 현재 밤이므로 낮인 경우를 삽
                    q.append((x, y, skill, 0, dist + 1))
            else: # 벽이 아닐 때
                temp_stat = (statue + 1) % 2
                if not visited[nx][ny][skill]: # 벽이 아니므로 바로 진행
                    visited[nx][ny][skill] = True
                    q.append((nx, ny, skill, temp_stat, dist + 1))
    return -1
print(bfs(0, 0, k))