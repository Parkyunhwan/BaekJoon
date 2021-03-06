# rebas 형님
from collections import deque
for _ in range(int(input())):
    n = int(input())
    dist = [-1]*n  # dist를 n크기만큼 설정한다.
    dist[1 % n] = 0  #  1 부터 시작한다. (문제 조건)
    q = deque()
    q.append(1)
    ans = 0
    while q:
        x = q.popleft()
        if x % n == 0:  # 현재 값을 n으로 나누어 떨어지면 break
            ans = x
            break
        for i in [0, 1]:  # BFS의 방향은 2가지가 있다 0인 경우 & 1인 경우
            nx = x*10 + i  # 매 진행 시 마다 10을 곱한 후 0 또는 1을 더한다. x0 or x1
            if dist[nx % n] == -1:  # 진행 값의 나머지가 첫 방문인가?
                #  !! 나머지가 같다는 것의 의미는 nx가 어떤숫자든 상관없이 앞으로의 진행과정에서 똑같다는 의미
                #  따라서, 단 한번만 큐에 넣어주는 것이 의미없는 탐색을 없앨 수 있다.!!
                dist[nx % n] = nx  # 현재값을 나머지의 방문으로 기록
                q.append(nx)  #
    print(ans if ans else "BRAK")

# 1 % 17 = 1
# 10, 11 % 17 = 10, 11
# 100, 101, 110, 111 = 15, 16, 8, 9
# 1001, 1000, 1010, 1011, 1100, 1101, 1110, 1111 = (1011) 8, 1101 13
# 11011

# 굉장히 쉽지만 생각하기는 까다로운 문제
# 두 가지를 생각해내야 했다.
# 1. 1과 0만으로 이루어진 숫자를 어떻게 구성해서 검사할 것인가?
# -> 1과 0 두 개를 선택하는 BFS를 통해 값을 늘려간다.
# 2. 길면 2^100개 까지 갈 수 있는데 이것을 어떤 방식으로 방지 할 것인가?
# -> 어떤 수에서 나머지가 같다는 것은
from collections import deque
t = int(input())
arr =[]


def bfs(val):
    q = deque()
    check = [False]*(val+1)
    q.append(1)
    while q:
        p = q.popleft()
        for k in (0, 1):
            np = p * 10 + k
            if np % val == 0:
                print(np)
                return
            else:
                if not check[np % val]:
                    check[np % val] = True
                    q.append(np)
    print("BRAK")
for _ in range(t):
    val = int(input())
    bfs(val)
