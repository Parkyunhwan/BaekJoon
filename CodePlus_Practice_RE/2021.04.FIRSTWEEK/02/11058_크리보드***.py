# dp 풀이
n = int(input())

dp = [0] * (n + 1)

if n <= 6:
    print(n)
    exit(0)

for i in range(1, 7):
    dp[i] = i

for i in range(7, n + 1):
    for j in range(3, n + 1):
        dp[i] = max((j - 1) * dp[i - j], dp[i])

print(dp[n])



# 시간초과
'''
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
'''