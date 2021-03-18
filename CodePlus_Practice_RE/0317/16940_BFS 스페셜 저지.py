'''
    1 번 방법 : 각 그래프의 순서를 order대로 정렬한다. https://vixxcode.tistory.com/28
    2 번 방법 : bfs를 수행해서 각 단계의 원소 리스트를 구하고 큐에는 order순서대로 다 넣을 수 있는 지 검사한다.
                만약 넣을 수 없다면 정답의 순서는 수행 불가하다.
'''

from collections import defaultdict
from collections import deque
n = int(input())

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))

if order[0] != 1:
    print(0)
    exit(0)

visited = [False] * (n + 1)
q = deque()

q.append(order[0])
visited[order[0]] = True

idx = 1
while q:
    curr = q.popleft()

    if not graph[curr]:
        continue

    # 이번 단계에서 방문 가능한 모든 정점
    nex = []
    for i in graph[curr]:
        if not visited[i]:
            nex.append(i)
            visited[i] = True

    # 모든 정점을 순서에 맞게 큐에 넣어주는 과정이며 만약 넣을 수 없는 값이 순서에 있다면 틀린 예시이다.
    l = len(nex) # 이전에 방문하지 않았던 새로 추가된 정점의 갯수
    for k in range(idx, idx + l):
        if order[k] in nex: # 새로 추가 된 정점은 order[k]에 있어야만 한다.
            q.append(order[k])
        else:
            print(0)
            exit(0)
    idx += l
print(1)