from collections import deque
import heapq
t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = []
    de = deque()
    for idx, val in enumerate(arr):
        heapq.heappush(q, -val)
        de.append((idx, val))
    num = 1
    while de:
        idx, val = de.popleft()
        mx_val = -heapq.heappop(q)
        if mx_val == val:
            if idx == M:
                print(num)
                break
            num += 1
        else:
            heapq.heappush(q, -mx_val)
            de.append((idx, val))

