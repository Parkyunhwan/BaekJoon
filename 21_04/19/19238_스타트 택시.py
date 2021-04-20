from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_arrival(baekjoon, ax, ay, fuel, idx):
    visited = [[-1] * N for _ in range(N)]
    sx, sy = baekjoon
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] != -1 or arr[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

    distance = visited[ax][ay]
    if fuel >= distance:
        fuel -= distance
        fuel += (distance * 2)
        customer[idx] = [-1, -1, -1, -1]
        return fuel
    else:
        return -1


def cal_min_distance(arr, baekjoon):
    visited = [[-1] * N for _ in range(N)]
    min_distance = 1e9
    prev = -1
    q = deque()
    q.append([baekjoon[0], baekjoon[1]])
    visited[baekjoon[0]][baekjoon[1]] = 0
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] != -1 or arr[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

    for i in range(1, M + 1):
        if customer[i][0] == -1:
            continue
        sx, sy = customer[i][0], customer[i][1]
        value = visited[sx][sy]
        if value == -1:
            return [-1, -1]
        if min_distance == 1e9:
            min_distance = value
            prev = i
        elif min_distance > value:
            min_distance = value
            prev = i
        elif min_distance == value:
            if customer[prev][0] > sx:
                prev = i
            elif customer[prev][0] == sx and customer[prev][1] > sy:
                prev = i
    return [prev, visited[customer[prev][0]][customer[prev][1]]]



if __name__ == "__main__":
    N, M, fuel = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    customer = [[0] * 4 for _ in range(M + 1)]
    baekjoon = list(map(int, input().split())) # sx, sy
    baekjoon = [baekjoon[0] - 1, baekjoon[1] - 1]
    for i in range(1, M + 1):
        sx, sy, ax, ay = map(int, input().split())
        sx, sy, ax, ay = sx - 1, sy - 1, ax - 1, ay - 1
        customer[i] = [sx, sy, ax, ay]
    count = 0
    while count < M:

        idx, distance = cal_min_distance(arr, baekjoon)
        if idx == -1:
            break
        if fuel < distance:
            break
        fuel -= distance
        ax, ay = customer[idx][2], customer[idx][3]
        baekjoon = [customer[idx][0], customer[idx][1]]
        result = move_arrival(baekjoon, ax, ay, fuel, idx)
        if result == -1:
            break
        else:
            fuel = result
            baekjoon = [ax, ay]
        count += 1
    if count == M:
        print(fuel)
    else:
        print(-1)