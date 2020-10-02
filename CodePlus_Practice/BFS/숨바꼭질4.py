from collections import deque
n, k = map(int, input().split())
path = [-2]*100001


def search_path():
    i = k
    st = deque()
    st.appendleft(i)
    while path[i] != -1:
        st.appendleft(path[i])  # 이전 값
        i = path[i]
    for i in st:
        print(i, end=" ")


def BFS():
    global path
    q = deque()
    q.append((n, 0))
    path[n] = -1
    while q:
        su, count = q.popleft()
        if su == k:
            print(count)
            search_path()
            return
        if su+1 <= 100000 and path[su+1] == -2:
            q.append((su+1, count+1))
            path[su+1] = su
        if su-1 >= 0 and path[su-1] == -2:
            q.append((su-1, count+1))
            path[su-1] = su
        if su*2 <= 100000 and path[su*2] == -2:
            q.append((su*2, count+1))
            path[su*2] = su

BFS()