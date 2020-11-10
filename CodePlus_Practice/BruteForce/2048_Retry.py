# 언제나 어려운 행 열 구분
from collections import deque


def merge(q, sx, sy, dx, dy):

    while q:
        val = q.popleft()
        if arr[sx][sy] == 0:
            arr[sx][sy] = val
        elif arr[sx][sy] == val:
            arr[sx][sy] = 2*val
            sx += dx
            sy += dy
        else:
            sx += dx
            sy += dy
            arr[sx][sy] = val


def move(dir):
    q = deque()
    if dir == 0:
        for j in range(n):
            for i in range(n):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                arr[i][j] = 0
            merge(q, 0, j, 1, 0)
    elif dir == 1:
        for j in range(n):
            for i in range(n-1,-1,-1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                arr[i][j] = 0
            merge(q, n-1, j,  -1, 0)
    elif dir == 2:
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                arr[i][j] = 0
            merge(q, i, 0, 0, 1)
    elif dir == 3:
        for i in range(n):
            for j in range(n-1,-1,-1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                arr[i][j] = 0
            merge(q, i, n-1, 0, -1)


def dfs(index):
    global mx, arr
    if index == 5:
        for a in arr:
            mx = max(max(a), mx)
        return
    else:
        backup = [a[:] for a in arr]
        for k in range(4): #  상 하 좌 우
            move(k)
            dfs(index+1)
            arr = [back[:] for back in backup]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mx = 0


dfs(0)
print(mx)