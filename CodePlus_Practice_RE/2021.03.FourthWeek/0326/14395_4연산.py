from collections import deque
from collections import defaultdict
s, t = map(int, input().split())

if s == t:
    print(0)
    exit(0)

q = deque()
q.append((s, []))

dic = defaultdict(int)
dic[s] += 1
while q:
    curr, oper = q.popleft()

    if curr == t:
        print(''.join(oper))
        exit(0)

    if curr <= t and curr * curr <= 10e9:
        if dic[curr * curr] == 0:
            tmp = oper[:]
            tmp.append('*')
            dic[curr * curr] += 1
            q.append((curr * curr, tmp))
    if curr <= t and curr + curr <= 10e9:
        if dic[curr + curr] == 0:
            tmp = oper[:]
            tmp.append('+')
            dic[curr + curr] += 1
            q.append((curr + curr, tmp))
    if curr - curr >= 0:
        if dic[curr - curr] == 0:
            tmp = oper[:]
            tmp.append('-')
            dic[curr + curr] += 1
            q.append((curr - curr, tmp))
    if curr != 0:
        if dic[curr / curr] == 0:
            tmp = oper[:]
            tmp.append('/')
            dic[curr / curr] += 1
            q.append((curr / curr, tmp))

print(-1)
