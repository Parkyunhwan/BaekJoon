from collections import deque
import copy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mx = 1e9
for row in arr:
    mx = min(min(row), mx)

def move(direction):
    q = deque()
    if direction == 0:  # left
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            curr = 0
            while q:
                val = q.popleft()
                if arr[i][curr] == 0:
                    arr[i][curr] = val
                else:
                    if arr[i][curr] == val:
                        arr[i][curr] = val * 2
                        curr += 1
                    else:
                        curr += 1
                        arr[i][curr] = val
    elif direction == 1:  # right
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            curr = n - 1
            while q:
                val = q.popleft()
                if arr[i][curr] == 0:
                    arr[i][curr] = val
                else:
                    if arr[i][curr] == val:
                        arr[i][curr] = val * 2
                        curr -= 1
                    else:
                        curr -= 1
                        arr[i][curr] = val
    elif direction == 2:  # up
        for j in range(n):
            for i in range(n):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            curr = 0
            while q:
                val = q.popleft()
                if arr[curr][j] == 0:
                    arr[curr][j] = val
                else:
                    if arr[curr][j] == val:
                        arr[curr][j] = val * 2
                        curr += 1
                    else:
                        curr += 1
                        arr[curr][j] = val
    elif direction == 3:  # down
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
                    arr[i][j] = 0
            curr = n - 1
            while q:
                val = q.popleft()
                if arr[curr][j] == 0:
                    arr[curr][j] = val
                else:
                    if arr[curr][j] == val:
                        arr[curr][j] = val * 2
                        curr -= 1
                    else:
                        curr -= 1
                        arr[curr][j] = val
    return arr


def game2048(count):
    global mx, arr
    if count == 5:
        for row in arr:
            mx = max(max(row), mx)
        return

    back = [a[:] for a in arr]
    for k in range(4):
        arr = move(k)
        game2048(count + 1)
        arr = [b[:] for b in back]
game2048(0)
print(mx)