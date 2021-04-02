from collections import deque
from collections import defaultdict
n = int(input())

q = deque()
q.append((0, 0, 0, 0))
dic = defaultdict(int)

result = 0
while q:
    text, buf, select, count = q.popleft()
    if count > n:
        break
    result = max(result, text)
    val = str(text) + str(buf) + str(select)
    if dic[val] > 0:
        continue
    dic[val] += 1
    q.append((text + 1, buf, 0, count + 1))
    q.append((text, buf, text, count + 1))
    q.append((text, select, 0, count + 1))
    q.append((text + buf, buf, 0, count + 1))


print(result)
