# https://cocosy.tistory.com/12
# velog 다시 풀기 백트래킹
n = int(input())
a = [[0]*n for _ in range(n)]
b = list(input())
v, k = [], 0

def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if a[i][idx] == '+' and s <= 0:
            return False
        if a[i][idx] == '0' and s != 0:
            return False
        if a[i][idx] == '-' and s >= 0:
            return False
    return True


def solve(idx):
    if idx == n:
        print(''.join(map(str, v)))
        exit(0)
    for i in range(-10,11):
        v.append(i)
        if possible(idx):
            solve(idx+1)
        v.pop()

for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        k += 1
solve(0)