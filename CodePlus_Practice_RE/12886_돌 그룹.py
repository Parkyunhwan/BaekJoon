from collections import deque
def bfs():
    q = deque()
    q.append((A, B))
    check[A][B] = True
    while q:
        x, y = q.popleft()
        z = D - x - y # x, y로 z까지 구할 수 있음
        if x == y == z:
            print(1)
            return
        for a, b in (x, y), (x, z), (y, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue
            c = D - a - b
            X = min(a, b, c)
            Y = max(a, b, c)
            if not check[X][Y]:
                q.append((X, Y))
                check[X][Y] = True
    print(0)

def solve():
    if D % 3: # 3개를 더했으므로 3개가 같으려면 3으로 나누어 떨어져야만 한다!!
        print(0)
    else:
        bfs()

A, B, C = map(int, input().split())
D = A + B + C
check = [[False] * D for _ in range(D)]
solve()



# from collections import deque
# dol = list(map(int, input().split()))
#
# visited = [[[False] * 1501 for _ in range(1501)] for _ in range(1501)]
#
# q = deque()
# q.append(dol)
# li = [[0, 1], [0, 2], [1, 2]]
# while q:
#     dol = q.popleft()
#     if dol[0] == dol[1] == dol[2]:
#         print(1)
#         exit(0)
#     for val in li:
#         ndol = dol[:]
#         if ndol[val[0]] < ndol[val[1]]:
#             ndol[val[1]] -= ndol[val[0]]
#             ndol[val[0]] *= 2
#         else:
#             ndol[val[0]] -= ndol[val[1]]
#             ndol[val[1]] *= 2
#         if not visited[ndol[0]][ndol[1]][ndol[2]]:
#             visited[ndol[0]][ndol[1]][ndol[2]] = True
#             q.append(ndol)
#
# print(0)
