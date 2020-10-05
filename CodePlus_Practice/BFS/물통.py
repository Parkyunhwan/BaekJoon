from collections import deque

asize, bsize, csize = map(int, input().split())

q = deque()
q.append((0, 0, csize))
check = [[[False] * 201 for _ in range(201)] for _ in range(201)]
result = []


def move(i, _a, _b, _c):
    if i == 0:  # a -> b
        empty = bsize - _b
        if empty >= _a:
            _b += _a
            _a = 0
        else:
            _a -= empty
            _b = bsize
    elif i == 1:  # a -> c
        empty = csize - _c
        if empty >= _a:
            _c += _a
            _a = 0
        else:
            _a -= empty
            _c = csize
    elif i == 2:  # b -> c
        empty = csize - _c
        if empty >= _b:
            _c += _b
            _b = 0
        else:
            _b -= empty
            _c = csize
    elif i == 3:  # c -> a
        empty = asize - _a
        if empty >= _c:
            _a += _c
            _c = 0
        else:
            _c -= empty
            _a = asize
    elif i == 4:  # c -> b
        empty = bsize - _b
        if empty >= _c:
            _b += _c
            _c = 0
        else:
            _c -= empty
            _b = bsize
    elif i == 5:  # b -> a
        empty = asize - _a
        if empty >= _b:
            _a += _b
            _b = 0
        else:
            _b -= empty
            _a = asize
    return _a, _b, _c


c_check = [False] * 201
while q:
    a, b, c = q.popleft()
    if a == 0 and not c_check[c]:
        c_check[c] = True
        result.append(c)
    for index in range(6):
        i, j, k = move(index, a, b, c)
        if not check[i][j][k]:
            check[i][j][k] = True
            q.append((i, j, k))

result.sort()
for i in result:
    print(i, end=" ")
