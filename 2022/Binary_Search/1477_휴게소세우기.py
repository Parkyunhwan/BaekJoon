import heapq
import math
N, M, L = map(int, input().split())
li = list(map(int, input().split()))

li.extend([0, L])
q = []
li.sort()
for i in range(len(li) - 1):
    diff = li[i + 1] - li[i]
    heapq.heappush(q, [-diff, diff, 2])


for _ in range(M):
    diff, origin, div = heapq.heappop(q)
    diff = -diff
    val = math.ceil(origin / div)
    heapq.heappush(q, [-val, origin, div + 1])

print(-heapq.heappop(q)[0])
