N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stack_arr = [[[] for _ in range(N)] for _ in range(N)]
horse = []

for i in range(K):
    x, y, dir = map(int, input().split())
    horse.append((x - 1, y - 1, dir - 1))
    stack_arr[x - 1][y - 1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
flag = False
time = 1

print(horse)
for i in range(N):
    for j in range(N):
        print(stack_arr[i][j], end=" ")
    print()


while time <= 9:
    print()
    print("time : " + str(time))
    for i in range(K):
        x, y, curr_dir = horse[i]
        print(i)

        for a in range(N):
            for b in range(N):
                print(stack_arr[a][b], end=" ")
            print()

        tmp = []
        tmp2 = []
        for idx, val in enumerate(stack_arr[x][y]):
            print(idx, val, i)
            if val == i:
                print("index value " + str(val))
                tmp = stack_arr[x][y][idx:]
                tmp2 = stack_arr[x][y][:idx]

        nx, ny = x + dx[curr_dir], y + dy[curr_dir]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:# blue
            if curr_dir == 0:
                curr_dir = 1
            elif curr_dir == 1:
                curr_dir = 0
            elif curr_dir == 2:
                curr_dir = 3
            elif curr_dir == 3:
                curr_dir = 2

            nx, ny = x + dx[curr_dir], y + dy[curr_dir]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:  # blue
                for index in tmp:
                    if index == i:
                        horse[index] = x, y, curr_dir
                    else:
                        horse[index] = x, y, horse[index][2]
                continue

        print(x, y, stack_arr[x][y])

        if arr[nx][ny] == 0: # white
            for index in tmp:
                horse[index] = nx, ny, horse[index][2]
            stack_arr[nx][ny].extend(tmp)
            stack_arr[x][y] = tmp2[:]
        elif arr[nx][ny] == 1: # red
            for index in tmp:
                horse[index] = nx, ny, horse[index][2]
            stack_arr[nx][ny].extend(reversed(tmp))
            stack_arr[x][y] = tmp2[:]


        print(arr[nx][ny])

        print(nx, ny, stack_arr[nx][ny])
        print()

        for a in range(N):
            for b in range(N):
                print(stack_arr[a][b], end=" ")
            print()
        if len(stack_arr[nx][ny]) == N:
            flag = True
            break


    if flag:
        break
    time += 1
if time > 1000:
    print(-1)
else:
    print("return")
    print(time)
