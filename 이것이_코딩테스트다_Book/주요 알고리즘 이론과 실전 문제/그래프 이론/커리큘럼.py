# 위상정렬 (방향 그래프의 모든 노드를 `방향성에 거스르지 않도록 순서대로 나열`)
from collections import deque
import copy
v = int(input())
graph = [[] for _ in range(v+1)]
indegree = [0]*(v+1)
time = [0]*(v+1)

for i in range(1, v+1):
    in_val = list(map(int, input().split()))
    time[i] = in_val[0]
    for k in in_val[1:-1]:
        graph[k].append(i) # 맨 앞에 시작은 진입차수가 0이므로 리스트에 아무것도 없고 그 다음 리스트부터 시작한다.
        indegree[i] += 1


def topology():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, v+1):
        if not indegree[i]:
            q.append(i)
    while q:
        now = q.popleft()
        for g in graph[now]:
            result[g] = max(result[g], result[now] + time[g])
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)


    for i in range(1, v+1):
        print(result[i])
topology()