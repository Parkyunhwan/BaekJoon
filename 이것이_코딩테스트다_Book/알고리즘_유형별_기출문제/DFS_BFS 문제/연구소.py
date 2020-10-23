# 1회차 => 못품
# 벽을 어떻게 조합해서 새울 것인가에 대해 결정하지 못했다.
# 조합으로 하려했지만 0이 너무 많아서 안되고 중복되는 값도 많았다.
# dfs를 통해 1의 위치를 선택하는 것이 올바른 방법이였다.
# 이렇게 생각해보자. -> '벽이 3개가 선택되었을 때 0의 갯수를 반환받는다'
# 위의 식에 단지 '벽이 3개가 선택되었을 때 "바이러스가 퍼진 후" 0의 갯수를 반환받는다 로 바뀐 것이다.
# 하지만 우리는 바이러스가 퍼진 후의 연구소로 계속해서 실험할 수 없기 때문에 바이러스가 퍼지기 전의 상황을 기억해둔다.

# 2회차 => 품
n, m = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mx = 0


def virus_dfs(a, sx, sy):
    h = len(a)
    w = len(a[0])
    for k in range(4):
        nx, ny = sx + dx[k], sy + dy[k]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        elif a[nx][ny] != 0:
            continue
        else:
            a[nx][ny] = 2
            virus_dfs(a, nx, ny)
    return


def count_safe(ar):
    sm = 0
    for a in ar:
        sm += a.count(0)
    return sm


def solution(index, arr):
    global mx
    h = len(arr)
    w = len(arr[0])
    if index == 3:
        back = [a[:] for a in arr]
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 2:
                    virus_dfs(back, i, j)
        mx = max(count_safe(back), mx)
        return

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 0:
                arr[i][j] = 1
                solution(index+1, arr)
                arr[i][j] = 0


solution(0, ar)
print(mx)

############################3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mx = -1


def virus(vstart):
    x, y = vstart
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus((nx, ny))


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def solution(arr, wall_count):
    global mx
    if wall_count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]
        for v_component in v:
            virus(v_component)
        score = get_score()
        mx = max(mx, score)
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                solution(arr, wall_count+1)
                arr[i][j] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = []
temp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            v.append((i, j))
solution(arr, 0)
print(mx)

