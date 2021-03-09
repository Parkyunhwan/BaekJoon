import itertools
import sys
n = int(input())
arr = list(map(int, input().split()))

oper = list(map(int, input().split()))
oper_c = []
for i, val in enumerate(oper):
    if i == 0:
        for _ in range(val):
            oper_c.append('+')
    elif i == 1:
        for _ in range(val):
            oper_c.append('-')
    elif i == 2:
        for _ in range(val):
            oper_c.append('*')
    elif i == 3:
        for _ in range(val):
            oper_c.append('/')
mx = -sys.maxsize
mn = sys.maxsize
perm = itertools.permutations(oper_c, n - 1)
for per in list(perm):
    sm = arr[0]
    for i in range(n - 1):
        if per[i] == '+':
            sm = (sm + arr[i + 1])
        elif per[i] == '-':
            sm = (sm - arr[i + 1])
        elif per[i] == '*':
            sm = (sm * arr[i + 1])
        elif per[i] == '/':
            if sm < 0:
                sm = -sm
                sm = -1 * (sm // arr[i + 1])
            else:
                sm = (sm // arr[i + 1])

    mx = max(sm, mx)
    mn = min(sm, mn)
print(mx)
print(mn)