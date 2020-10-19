# 1회차 -> 실패
# 시간초과가 발생했다. 아쉽게도 한번에 처리할 수 있는 부분(연합의 수와 합을 세는일)을 여러번에 걸쳐 처리했다.


from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def BFS(sx, sy, count):
    q = deque()
    q.append((sx, sy))
    check[sx][sy] = count
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or check[nx][ny] != 0:
                continue
            elif l <= abs(arr[nx][ny] - arr[tx][ty]) <= r:
                check[nx][ny] = count
                q.append((nx, ny))


def solution(index):
    for i in range(n):
        for j in range(n):
            check[i][j] = 0
    count = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                count += 1
                BFS(i, j, count)
    #  for문을 빠져나오면 연합이 결정됨
    flag = False
    for i in range(n):
        for j in range(n):
            if check[i][j] != 0:
                flag = True
    if not flag:
        print(index)
        return
    # 연합 평균 구하기
    average = []
    for c in range(1, count + 1):
        sm, num = 0, 0
        for i in range(n):
            for j in range(n):
                if check[i][j] == c:
                    num += 1
                    sm += arr[i][j]
        if num != 0:
            average.append(sm//num)

    for c in range(1, count + 1):
        for i in range(n):
            for j in range(n):
                if check[i][j] == c:
                    arr[i][j] = average[c - 1]
    solution(index + 1)


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
solution(0)
