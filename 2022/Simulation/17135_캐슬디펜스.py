from collections import deque
import sys
N, M, D = map(int, input().split())
dx = [0, -1, 0]
dy = [-1, 0, 1]
land = []
enemy_num = 0
for _ in range(N):
    li = list(map(int, input().split()))
    enemy_num += li.count(1)
    land.append(li)


def simulation(archers, tmp_land):
    land = tmp_land
    # 궁수의 공격
    kill_num = 0
    erase_num = 0

    while kill_num + erase_num != enemy_num and land:
        kill_enemy = set()
        length = len(land)
        for y in archers:
            archer_map = [[0] * M for _ in range(length)]
            sx, sy = length - 1, y
            q = deque()
            q.append((sx, sy, 1))
            archer_map[sx][sy] = 1

            while q:
                x, y, dist = q.popleft()
                if dist > D:
                    break
                if land[x][y] == 1:
                    kill_enemy.add((x, y))
                    break
                for k in range(3):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or ny < 0 or nx >= length or ny >= M or archer_map[nx][ny]:
                        continue
                    archer_map[nx][ny] = dist + 1
                    q.append((nx, ny, dist + 1))

        for enemy_pos in kill_enemy:
            x, y = enemy_pos
            if land[x][y] == 1:
                kill_num += 1
            land[x][y] = 0

        erase_row = land.pop()
        erase_num += erase_row.count(1)

    return kill_num

def Archer_position(idx, archers):
    global result
    if len(archers) == 3:
        tmp_land = [l[:] for l in land]
        kill_num = simulation(archers, tmp_land)
        result = max(result, kill_num)
        return

    for i in range(idx, M):
        archers.append(i)
        Archer_position(i + 1, archers)
        archers.pop()

result = 0
Archer_position(0, [])
print(result)
# 0. 궁수 배치

# 1. 궁수의 공격 D이하 가까운 왼쪽 적
# 2. 적의 이동