# BFS
# recommit
# velog 작성 시 BFS DFS 차이와 처음에 틀린 이유 적기
# sys.stdin.readline().strip() 이란?
# stdin이 input보다 빠르고 readline()을 통해 한 줄을 읽어옴
# strip()을 통해 readline()의 맨 뒤 개행문자를 삭제할 수 있음
import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = {(x, y, board[x][y])}

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)

# DFS 좀 빠르긴 한데 비슷
import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
y, x = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().strip())) for i in range(y)]
ch = [0] * 26


def solve(ny, nx, val):
    global mx
    mx = max(mx, val)

    for i in range(4):
        temp_y = ny + dy[i]
        temp_x = nx + dx[i]
        if 0 <= temp_y < y and 0 <= temp_x < x and ch[arr[temp_y][temp_x]] == 0:
            ch[arr[temp_y][temp_x]] = 1
            solve(temp_y, temp_x, val + 1)
            ch[arr[temp_y][temp_x]] = 0


mx = 1
ch[arr[0][0]] = 1
solve(0, 0, mx)
print(mx)

# 시간 초과 코드 였지만 작은 차이로 안남
def my_solve(ny,nx, val):
    global mx
    mx=max(mx, val)
    for i in range(4):
        temp_y = ny + dy[i]
        temp_x = nx + dx[i]
        if 0 <= temp_y < y and 0 <= temp_x < x and arr[temp_y][temp_x] in st:
            st.remove(arr[temp_y][temp_x])
            my_solve(temp_y, temp_x, val+1)
            st.add(arr[temp_y][temp_x])


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
y, x = map(int, input().split())
mx = -1
arr = []
st = set()
for i in range(y):
    arr.append(list(input()))
    st |= set(arr[i])
st.remove(arr[0][0])
my_solve(0, 0, 1)

print(mx)
