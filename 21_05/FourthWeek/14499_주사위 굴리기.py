'''
    시뮬레이션 문제

    내가 푼 것 처럼 2차원으로 옮겨서 해결해도 되지만 따로 score 배열을 만들어줘야했다.

    이 방법말고 1차원 배열로 값들을 그대로 이동시켜 답을 구할 수도 있다. (https://jjangsungwon.tistory.com/21)

'''
N, M, x, y, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

operation = list(map(int, input().split()))

dice = [[0] * 3 for _ in range(4)]

dice[0][1], dice[1][0], dice[1][1], dice[1][2], dice[2][1], dice[3][1] = 2, 4, 1, 3, 5, 6
score = [0] * 7

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for dir in operation:
    nx, ny = x + dx[dir], y + dy[dir]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
    x, y = nx, ny
    if dir == 1: # 동
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif dir == 2: # 서
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif dir == 3: # 북
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    else: # 남
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    if arr[x][y] == 0:
        arr[x][y] = score[dice[3][1]]
    else:
        score[dice[3][1]] = arr[x][y]
        arr[x][y] = 0
    print(score[dice[1][1]])
