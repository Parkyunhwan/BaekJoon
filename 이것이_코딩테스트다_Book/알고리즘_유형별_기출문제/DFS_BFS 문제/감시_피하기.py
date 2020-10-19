# 1회차 -> 성공

# 1. 핵심은 장애물 3개를 어떻게 설치하느냐 -> DFS를 이용해서 모든 경우의 수를 따진다.
# 2. 두번째 핵심은 처음 맵의 정보를 복사해서 선생님의 감시를 검사하는 것
#    복사를 통해 다음 장애물 설치 후 검사시 영향을 주지 않게 한다.
n = int(input())
arr = [list(input().split()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생이 있으면 True를 반환


def check_student(temp, t, k):
    tx, ty = t[0], t[1]
    nx, ny = tx + dx[k], ty + dy[k]
    while 0 <= nx < n and 0 <= ny < n:
        if temp[nx][ny] == 'S':
            return True
        elif temp[nx][ny] == 'X':
            temp[nx][ny] = 'T'
        elif temp[nx][ny] == 'O':
            break
        nx = nx + dx[k]
        ny = ny + dy[k]
    return False


def teacher_watch():
    teacher = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                teacher.append((i, j))

    temp = [a[:] for a in arr]
    for t in teacher:
        for k in range(4):
            if check_student(temp, t, k):
                return True
    return False


def select_wall(index):
    flag = False
    if index == 3:  # 벽을 3개 모두 선택했다면
        if not teacher_watch():
            return True
        return False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                flag = select_wall(index+1)
                arr[i][j] = 'X'
                if flag:
                    return True
    return False


if select_wall(0):
    print("YES")
else:
    print("NO")
