from collections import deque

N = int(input())
arr = list(map(int, input().split()))

q = deque()
for i in range(len(arr)):
    q.append((i + 1, arr[i],))

curr_idx, value = q.popleft()
while q:
    print(curr_idx, end=' ')

    if value > 0:
        for _ in range(value - 1):
            q.append(q.popleft())
        curr_idx, value = q.popleft()
    else:
        for _ in range(-value - 1):
            q.appendleft(q.pop())
        curr_idx, value = q.pop()

print(curr_idx)
