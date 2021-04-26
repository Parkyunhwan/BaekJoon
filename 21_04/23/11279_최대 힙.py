import heapq
import sys
N = int(input())
q = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())

    if x > 0:
        heapq.heappush(q, -x)
    else:
        if not q:
            print(0)
        else:
            val = -heapq.heappop(q)
            print(val)

