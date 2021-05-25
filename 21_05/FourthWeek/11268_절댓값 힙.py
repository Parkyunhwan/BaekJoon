import heapq
import sys
N = int(input())
count = 0

q = []
for _ in range(N):
    val = int(sys.stdin.readline())
    if val == 0:
        if q:
            val = heapq.heappop(q)
            print(val[1])
        else:
            print(0)
        continue
    heapq.heappush(q, [abs(val), val])
