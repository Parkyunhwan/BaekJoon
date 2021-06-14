'''
    궁수 3명의 위치를 정한다 (조합)

    정해진 위치에서 적을 향해 활을 쏜다.
    활을 쏘는 순서는 다음과 같다.
    1. 범위 안에서 가장 가까운 적부터 죽인다.
    2. 가까운 적이 여럿이라면 (왼 위 오) 순서로 죽인다.
    3. 여러 궁수가 적 하나에 화살을 쏠 수도 있다.

    visited 배열과 checked 배열은 분명히 다른 배열이다.

    visited 배열은 BFS시 중복 방문으로 인한 무한루프 방지를 위한 것이고
    checked 배열은 여러 궁수가 쏜 화살의 위치를 표시하기 위함이다.
'''
from itertools import combinations
from collections import deque
import copy
N, M, D = map(int, input().split())

arr_origin = [list(map(int, input().split())) for _ in range(N)]

num = [i for i in range(M)]
comb = combinations(num, 3)


dx = [0, -1, 0]
dy = [-1, 0, 1]

result = 0
for human in list(comb):
    level = N - 1

    checked = [[False] * M for _ in range(N)] # 화살에 맞은 적 체크

    arr = copy.deepcopy(arr_origin) # 궁수에 위치에 따라 '적의 위치를 리셋'

    while level >= 0: # 적의 이동 (사실상 성이 이동하지만..)

        # 각 궁수의 위치 마다 반복
        for i in range(len(human)):
            curr_y = human[i]
            curr_x = level
            q = deque()
            q.append((curr_x, curr_y))


            visited = [[False] * M for _ in range(N)] # 각 궁수에 대해 BFS에 대한 방문체크를 위해 사용

            # 각 궁수의 위치에서 가장 가까운 적을 찾아 그 위치에 화살을 쏘기
            while q:
                x, y = q.popleft()
                visited[x][y] = True

                if arr[x][y] == 1:
                    checked[x][y] = True
                    break
                for k in range(3):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                        continue
                    if abs(curr_x - nx) + abs(curr_y - ny) >= D: # 거리가 D 이상 벌어지면 안됨
                        continue
                    q.append((nx, ny))

        # 각 궁수마다 화살을 쏜 후 화살을 쏜 위치에 적은 사살 (반드시 모든 궁수가 화살을 쏜 후 실행할 것)
        for i in range(N):
            for j in range(M):
                if checked[i][j]:
                    arr[i][j] = 0
        level -= 1

    sm = 0
    for i in range(N):
        for j in range(M):
            if checked[i][j]:
                sm += 1

    result = max(result, sm)

print(result)


