#  상근이는 가장자리 어디서나 갈 수 있도록 '.'을 바같에 추가해준다.
#  모르겟다. BFS의 실행 순서를 종잡을 수가 없다.. -> 순서를 뒤죽 박죽이라면 일단 저장해두는 것이 옳다.
#  -->(answer) : 현재 진행할 수 없지만 나중에 진행할 수 있는 것이므로 다른 큐에 일단 저장해둔다.
#  --> 또한 여기서 알파벳 별로 어떻게 구분할 것인가에 대한 구분은 deque배열을 통해 해결할 수 있다.

#  열쇠를 찾기전에 문을 검사하고 그 후에 열쇠를 찾는 경우를 어떻게 검사해야 할까?
#  --> 문의 위치를 다른 큐에 저장해두고 열쇠를 찾으면 다시 현재 진행 큐에 넣는다.

#  Check 배열을 방문 마다 Check 해두면 열쇠를 찾고도 방문하지 못하지 않을까?
#  -->(answer) : 열쇠가 없더라도 방문 Check를 해두고 알파벳 큐에 넣어 방문예약을 해두면 열쇠를 찾았을 때만 방문이 가능하게 할 수 있다.

from sys import stdin
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def BFS():
    q = deque()
    count = 0
    kdeq = [deque() for _ in range(26)]
    q.append((0, 0))
    check = [[False]*(w+2) for _ in range(h+2)]
    check[0][0] = True
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if nx < 0 or nx > h + 1 or ny < 0 or ny > w + 1:
                continue
            if arr[nx][ny] == '*' or check[nx][ny]:
                continue

            check[nx][ny] = True

            if arr[nx][ny] == '$':
                count += 1
            elif 'A' <= arr[nx][ny] <= 'Z':
                if not mykeys[ord(arr[nx][ny])-ord('A')]:
                #  if not arr[nx][ny].lower() in mykeys:
                    kdeq[ord(arr[nx][ny]) - ord('A')].append((nx, ny))
                    continue
            elif 'a' <= arr[nx][ny] <= 'z':
                d = kdeq[ord(arr[nx][ny])-ord('a')]
                mykeys[ord(arr[nx][ny])-ord('a')] = True
                #  mykeys.add(arr[nx][ny])
                while d:
                    q.append(d.popleft())
            q.append((nx, ny))
    return count



n = int(input())
for _ in range(n):
    h, w = map(int, stdin.readline().rstrip().split())
    arr = ['.'*(w+2)]
    for _ in range(h):
        arr.append('.'+stdin.readline().strip()+'.')
    arr.append('.'*(w+2))
    # mykeys = set(list(input()))
    mykeys = [False] * 26
    k = input()
    if k != '0':
        for i in k:
            mykeys[ord(i)-ord('a')] = True
    print(BFS())