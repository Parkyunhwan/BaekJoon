import sys
from itertools import combinations
from itertools import permutations
from collections import deque
n = int(input())

scv = list(map(int, input().split()))
dp = [[[sys.maxsize] * 61 for _ in range(61)] for _ in range(61)]

if n == 1:
    scv.extend([0, 0])
if n == 2:
    scv.extend([0])


mutal_attack = [9, 3, 1]
mutal_attack = list(permutations(mutal_attack, 3))

q = deque()
q.append(scv + [0])

dp[scv[0]][scv[1]][scv[2]] = 0
while q:
    a, b, c, count = q.popleft()

    if a == 0 and b == 0 and c == 0:
        print(count)
        exit(0)
    for x, y, z in mutal_attack:
        na, nb, nc = a - x, b - y, c - z
        if na < 0:
            na = 0
        if nb < 0:
            nb = 0
        if nc < 0:
            nc = 0

        if dp[na][nb][nc] == sys.maxsize:
            dp[na][nb][nc] = count + 1
            q.append([na, nb, nc, count + 1])




