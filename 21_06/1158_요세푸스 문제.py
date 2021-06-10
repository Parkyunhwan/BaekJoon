from collections import deque
N, K = map(int, input().split())

q = deque()

for i in range(1, N + 1):
    q.append(i)

print("<", end='')

while len(q) > 1:
    for _ in range(K - 1):
        val = q.popleft()
        q.append(val)

    val = q.popleft()
    print("%d," % val, end=' ')

print(q.popleft(), end='')
print(">")
