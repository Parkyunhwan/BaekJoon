import heapq

n = int(input())
sm = 0
plus = []
minus = []
zero = 0
one = 0
for _ in range(n):
    val = int(input())

    if val == 1:
        one += 1
    elif val > 0:
        heapq.heappush(plus, -val)
    elif val == 0:
        zero += 1
    else:
        heapq.heappush(minus, val)

if len(plus) % 2:
    heapq.heappush(plus, -1)
if len(minus) % 2:
    if zero > 0:
        heapq.heappush(minus, 0)
    else:
        heapq.heappush(minus, 1)

while plus:
    val1 = heapq.heappop(plus)
    val2 = heapq.heappop(plus)
    sm += (val1 * val2)

while minus:
    val1 = heapq.heappop(minus)
    val2 = heapq.heappop(minus)
    sm += (val1 * val2)

sm += one
print(sm)
