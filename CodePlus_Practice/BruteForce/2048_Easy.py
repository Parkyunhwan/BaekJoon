# dfs or bfs시 유지해야하는 현재 배열의 정보를 어떻게 보존해야 하는가?
# 모두 보관하면 메모리가 너무 많아지지 않을까?

# 구현력의 문제..
from collections import deque
from sys import stdin

mx = -1
n = int(input())
a = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
q = deque()


def get(i, j):
    if a[i][j]:
        q.append(a[i][j])
        a[i][j] = 0


def merge(i, j, di, dj):
    while q:
        val = q.popleft()
        if not a[i][j]:
            a[i][j] = val
            # 다음 원소는 아직들어가지 않았으므로 a[i+di][j+dj] == 0이다..
        elif a[i][j] == val:
            a[i][j] = val * 2
            i, j = i + di, j + dj
        else:
            i += di
            j += dj
            a[i][j] = val


def move(k):
    if k == 0:  # Up 이면 위로 숫자를 모으면서 점점 밑으로 내려오는 구조이다.
        for j in range(n):
            for i in range(n):
                get(i, j)  # 큐에 블럭을 담는 함수
            merge(0, j, 1, 0)  # 큐에 담은 블럭을 합치는 함수
    elif k == 1:  # down
        for j in range(n):
            for i in range(n-1, -1, -1): # 순서도 반대가 된다.
                get(i, j)
            merge(n - 1, j, -1, 0)
    elif k == 2:  # left
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    elif k == 3:  # right
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n - 1, 0, -1)


def dfs(index):
    global mx, a
    if index == 5:
        for i in range(n):
            mx = max(mx, max(a[i]))
        return
    b = [tmp[:] for tmp in a] # 복사 시 사용
    for i in range(4):
        move(i)
        dfs(index + 1)
        a = [tmp[:] for tmp in b]


dfs(0)
print(mx)
