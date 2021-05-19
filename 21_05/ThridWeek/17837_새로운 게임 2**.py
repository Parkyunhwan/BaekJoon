'''
    3시간 동안 코드 오류를 찾느라 헤멨다.

    문제의 조건을 잘못읽어서 답이 나오지 않았따..
    if len(stack_arr[nx][ny]) >= 4:
    조건이 4보다 크다면인데 K보다 크다면으로 착각함..

'''

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stack_arr = [[[] for _ in range(N)] for _ in range(N)]
horse = [[] for _ in range(K)]

for i in range(K):
    x, y, dir = map(int, input().split())
    horse[i] = [x - 1, y - 1, dir - 1]
    stack_arr[x - 1][y - 1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
flag = False

time = 1
while time <= 1000:
    for hi in range(K):
        x, y, curr_dir = horse[hi]

        nx, ny = x + dx[curr_dir], y + dy[curr_dir]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:# blue
            nhd = curr_dir-1 if curr_dir%2 else curr_dir+1
            horse[hi][2] = nhd
            nx, ny = x + dx[nhd], y + dy[nhd]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:  # blue
                continue

        temp = []
        for i, key in enumerate(stack_arr[x][y]):
            if key == hi:
                # 지금 말보다 위에 있는것들을 temp에 넣어서 이동준비
                temp = (stack_arr[x][y][i:])
                # 지금 말보다 아래있는것들만 남김
                stack_arr[x][y] = stack_arr[x][y][:i]
                break

        # 다음 위치가 빨간색이면, 순서 뒤집음
        if arr[nx][ny] == 1:
            temp = reversed(temp)

        # 다음 위치에 넣고, 위치 정보를 갱신함 방향은 그대로이므로 갱신X
        for i in temp:
            stack_arr[nx][ny].append(i)
            horse[i][:2] = [nx, ny]

        if len(stack_arr[nx][ny]) >= 4:
            flag = True
            break
    if flag:
        break
    time += 1

if time > 1000:
    print(-1)
else:
    print(time)
