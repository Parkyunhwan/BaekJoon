from collections import deque
wheel = [list(map(int, list(input()))) for _ in range(4)]
K = int(input())

def rotation(num, dir):
    global wheel
    if dir == 1: # 시계
        wheel[num] = [wheel[num][-1]] + wheel[num][:-1]
    elif dir == -1:
        wheel[num] = wheel[num][1:] + [wheel[num][0]]

for _ in range(K):
    q = deque()
    num, dir = map(int, input().split())
    q.append([num - 1, dir, -1])

    while q:
        num, dir, prev = q.popleft()
        nd = -1 if dir == 1 else 1
        if num == 0:
            if prev != 1 and wheel[num][2] != wheel[1][6]:
                q.append([1, nd, num])
        elif num == 3:
            if prev != 2 and wheel[num][6] != wheel[2][2]:
                q.append([2, nd, num])
        else:
            if prev != num - 1 and wheel[num][6] != wheel[num - 1][2]:
                q.append([num - 1, nd, num])
            if prev != num + 1 and wheel[num][2] != wheel[num + 1][6]:
                q.append([num + 1, nd, num])
        rotation(num, dir)

score = 0
for i in range(4):
    if wheel[i][0] == 1:
        score += (2 ** i)

print(score)