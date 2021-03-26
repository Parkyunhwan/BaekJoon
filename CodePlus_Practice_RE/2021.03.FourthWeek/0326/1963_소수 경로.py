'''
    품 -> 35분

'''

from collections import deque

sosu = [False] * (10001)

for i in range(2, 10001 // 2 + 1):
    if not sosu[i]:
        k = 2
        while i * k < 10001:
            sosu[i * k] = True
            k += 1


def check_sosu(value):
    if not sosu[value]:
        return True
    else:
        return False



for _ in range(int(input())):

    start, end = map(list, input().split())
    visited = [False] * 10001

    q = deque()

    visited[int(''.join(start))] = True
    q.append((start, 0))
    while q:
        val, count = q.popleft()

        if val == end:
            print(count)
            break

        for i in range(4):
            for j in range(10):
                nval = val[:]
                nval[i] = str(j)
                int_val = int(''.join(nval))
                if int_val < 1000 or not check_sosu(int_val) or visited[int_val]:
                    continue
                visited[int_val] = True

                q.append((nval, count + 1))


