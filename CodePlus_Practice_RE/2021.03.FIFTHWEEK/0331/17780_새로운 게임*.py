'''
    오랜 시간 걸려서 품.

    문제를 푸는 방법은 잘 설계했지만
    문제의 조건을 정확히 구현하지 못해서 해맸다.

    방향 전환이 필요할 때 현재 위치에 있는 모든 말들이 방향을 바꾸지 않고 현재 조건에 걸린 말만 방향을 바꿔야한다.

    [재풀이]
    새로운 게임 풀이 다시 보고 - 새로운 게임 2 풀기로 변경 (주말 0401)
'''

from collections import defaultdict
N, K = map(int, input().split())

horse = [[list() for _ in range(N)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


dic = defaultdict(list)
for i in range(1, K + 1):
    x, y, dir = map(int, input().split())
    x -= 1
    y -= 1
    dic[i].append((x, y, dir))
    horse[x][y].append(i)

turn = 1
while True:
    if turn > 1000:
        break
    for t in range(1, K + 1):
        x, y, dir = dic[t][0]
        flag = False
        if horse[x][y][0] != t:
            continue
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:
            if dir == 1:
                dir = 2
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 4
            elif dir == 4:
                dir = 3
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 2:
                dic[t].pop()
                dic[t].append((x, y, dir))
                flag = True

        if flag:
            continue
        if arr[nx][ny] == 0:  # white
            horse[nx][ny].extend(horse[x][y])
            for val in horse[x][y]:
                if val == t:
                    dic[val].pop()
                    dic[val].append((nx, ny, dir))
                else:
                    px, py, pdir = dic[val].pop()
                    dic[val].append((nx, ny, pdir))

            horse[x][y].clear()
        elif arr[nx][ny] == 1:  # red
            rev = list(reversed(horse[x][y]))
            horse[nx][ny].extend(rev)
            for val in horse[x][y]:
                if val == t:
                    dic[val].pop()
                    dic[val].append((nx, ny, dir))
                else:
                    px, py, pdir = dic[val].pop()
                    dic[val].append((nx, ny, pdir))
            horse[x][y].clear()

        if len(horse[nx][ny]) >= 4:
            print(turn)
            exit(0)
    turn += 1

print(-1)


