#  전형적인 BFS 문제이며 특별한 것은 딱하나 있었다. -> 어떻게 LEFT와 RIGHT를 네자리수가 아닐때에도 적절히 구현할 것인가..?
#  --> L : 첫번째 자릿수는 나누기 1000을 통해 나머지 세자리는 나머지 1000을 통해 구할 수 있다.
#  --> R : 첫번째 부터 세번째 자릿수까지는 나누기 10을 통해 네번째 자리는 나누기 10을 통해 얻을 수 있다.
#  명령어 D : Y = (X*2) % 10000
#  명령어 S : Y = X-1 (단, Y < 0일 경우, Y = 9999)
#  명령어 L : Y = (X%1000)*10 + X/1000
#  명령어 R : Y = X/10 + (X%10)*1000
#출처: https://rebas.kr/764 [PROJECT REBAS]

#  my code
from collections import deque

t = int(input())


def move(index, _a, pa):
    if index == 0:  # D
        return _a * 2 % 10000, pa + "D"
    elif index == 1:  # S
        return 9999 if _a == 0 else _a - 1, pa + "S"
    elif index == 2:  # L
        # 1234 -> 234 1, 0012 -> 0120
        first = _a // 1000
        second = _a % 1000
        _a = (second * 10) + first
        return _a, pa + "L"
    else:  # R
        # 1234 -> 4 123, 0012 -> 2001
        first = _a // 10
        second = _a % 10
        _a = (second * 1000) + first
        return _a, pa + "R"


def BFS():
    q = deque()
    q.append((a, ""))
    while q:
        sa, path = q.popleft()
        if sa == b:
            return path
        for i in range(4):
            na, npath = move(i, sa, path)
            if not check[na]:
                check[na] = True
                q.append((na, npath))


for _ in range(t):
    check = [False] * 10001
    a, b = map(int, input().split())
    print(BFS())


