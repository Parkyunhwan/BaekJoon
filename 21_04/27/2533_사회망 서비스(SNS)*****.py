'''
    트리 디피 (시간 초과)

    현재 노드가 얼리어답터이면 내 자식은 얼리어답터 일 수 도 아닐수도 있다.

    현재 노드가 얼리어답터가 아니면 자식은 무조건 얼리어답터이다.

'''
import sys
from sys import stdin

sys.setrecursionlimit(10**9)

N = int(stdin.readline())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(num):
    visited[num] = True
    for ne in graph[num]:
        if not visited[ne]:
            tree[num].append(ne)
            dfs(ne)


def get_minvalue(num, early):
    if dp[num][early] != -1:
        return dp[num][early]
    ret = 0
    if early:
        ret = 1
    for ne in tree[num]:
        if early:
            ret += min(get_minvalue(ne, early), get_minvalue(ne, not early))
        else:
            ret += get_minvalue(ne, True)
        dp[num][early] = ret
    return ret


dp = [[-1, -1] for _ in range(N + 1)]
dfs(1)
print(min(get_minvalue(1, True), get_minvalue(1, False)))

'''
시간 초과 안나는 코
'''
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(read())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

def spread_early_adapter(node):
    visited[node] = True
    early, not_early = 1, 0
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        child_early, child_not_early = spread_early_adapter(nxt)
        early += min(child_early, child_not_early)
        not_early += child_early
    return early, not_early

print(min(spread_early_adapter(s)))

'''

'''
