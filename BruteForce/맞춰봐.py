n = int(input())
a = [[0]*n for _ in range(n)]
b = list(input())
v = []
k = 0
for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        k += 1


def possible(index):
    s = 0
    for i in range(index, -1, -1):
        s += v[i]
        if a[i][index] == '+' and s <= 0:
            return False
        if a[i][index] == '0' and s != 0:
            return False
        if a[i][index] == '-' and s >= 0:
            return False
    return True


def dfs(index):
    if index == n:
        print(' '.join(map(str, v)))
        exit(0)
    else:
        for i in range(-10, 11):
            v.append(i)
            if possible(index):
                dfs(index + 1)
            v.pop()

dfs(0)