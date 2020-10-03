from collections import deque

t = int(input())


def D(v, path):
    return (2 * v) % 10000, path.append("D")


def S(v,path):
    return 9999 if v == 0 else v - 1, path.append("S")


def L(v,path):
    v = str(v)
    tmp = v[1:] + v[:1]
    return tmp, path.append("L")


def R(v,path):
    v = str(v)
    tmp = v[-1] + v[:-1]
    return tmp, path.append("R")


for _ in range(t):
    a, b = list(map(int, input().split()))
    q = deque()
    q.append((a, list()))
    while q:
        val, path = q.popleft()
        if val == b:
            print("".join(path))
            break
        for i in range(4):
            if i == 0:
                val, path = D(val, path)
            elif i == 1:
                val, path = S(val)
            elif i == 2:
                val, path = int(L(val))
            else:
                val, path = int(R(val))
        q.append((val, path))
