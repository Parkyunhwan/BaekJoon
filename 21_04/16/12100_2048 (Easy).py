from collections import deque
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_max_block():
    global max_value
    curr_max = 0
    for i in range(N):
        for j in range(N):
            if curr_max < arr[i][j]:
                curr_max = arr[i][j]
    max_value = max(max_value, curr_max)

def merge(q, i, j, di, dj):
    while q:
        curr = q.popleft()
        if arr[i][j] == 0:
            arr[i][j] = curr
        else:
            if arr[i][j] == curr:
                arr[i][j] = curr * 2
                i += di; j += dj
            else:
                i += di; j += dj
                arr[i][j] = curr


def move(dir):
    q = deque()

    if dir == 0: # up
        for j in range(N):
            for i in range(N):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            merge(q, 0, j, dx[dir], dy[dir])
    elif dir == 1: # down
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            merge(q, N - 1, j, dx[dir], dy[dir])
    elif dir == 2: # right
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            merge(q, i, N - 1, dx[dir], dy[dir])
    elif dir == 3: # left
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            merge(q, i, 0, dx[dir], dy[dir])




def dfs(idx):
    global arr
    if idx == 5:
        check_max_block()
        return

    back = [a[:] for a in arr]
    for d in range(4):
        move(d)
        dfs(idx + 1)
        arr = [b[:] for b in back]

max_value = 0
dfs(0)
print(max_value)