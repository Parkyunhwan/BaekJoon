# 1회차 => 정답
# 아쉬운점 체크 배열대신 디스턴스 배열로 처리했으면 큐에 하나넣고도 맞출 수 있었을 것 같다.
# 또한 중첩 while문 없이도 구했을 것 같다.

from collections import deque


def BFS(start):
    q = deque()
    q.append((start, 0))
    while q:
        ns, count = q.popleft()
        if count == k:
            result = [ns]
            while q:
                s, c = q.popleft()
                if c > k:
                    return result
                else:
                    result.append(s)
            return result
        for i in graph[ns]:
            if not check[i]:
                check[i] = True
                q.append((i, count+1))
    return [-1]


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

li = BFS(x)
li.sort()
for l in li:
    print(l)

