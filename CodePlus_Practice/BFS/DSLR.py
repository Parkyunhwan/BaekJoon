from collections import deque

t = int(input())


def D(v):
    return (2 * v) % 10000


def S(v):
    return 9999 if v == 0 else v - 1


def L(v):
    le = str(v)
    length = len(le)
    if length != 4:
        v = v*10
    else:
        v, d = divmod(v, 10**(length-1))
        v += d*10
    return v


def R(v):
    re = str(v)
    length = len(re)
    if length == 1:
        v = v*1000
    else:
        v, d = divmod(v, 10)
        v += (d*1000)
    return v


for _ in range(t):
    a, b = list(map(int, input().split()))
    check = [False] * 10000  #
    q = deque()
    q.append((a, ""))
    while q:
        val, path = q.popleft()
        if val == b:
            print(path)
            break
        for i in range(4):
            if i == 0:
                t = D(val)
                tmp = path[:] + "D"  #
            elif i == 1:
                t = S(val)
                tmp = path[:] + "S"
            elif i == 2:
                t = L(val)
                tmp = path[:] + "L"
            else:
                t = R(val)
                tmp = path[:] + "R"
            if not check[t]:
                check[t] = True
                q.append((t, tmp))
