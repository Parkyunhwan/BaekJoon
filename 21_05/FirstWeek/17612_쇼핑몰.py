'''
    https://blog.naver.com/jhc9639/221771452298
    우선순위큐
'''

import heapq
N, K = map(int, input().split())


arr = []
for _ in range(N):
    num, w = map(int, input().split())
    arr.append([w, num])

result = 0
curr_i = 1
curr_time = 0
prev_idx = 0
counter = []

for val in arr:
    w, num = val
    idx = prev_idx
    if len(counter) < K:
        heapq.heappush(counter, [curr_time + w, -idx, num])
        prev_idx = idx + 1

    if len(counter) == K:
        w, idx, num = heapq.heappop(counter)
        idx *= -1
        result += (curr_i * num)
        print(curr_i, num, result, w, idx)
        curr_i += 1
        curr_time = w
        prev_idx = idx

while counter:
    w, idx, num = heapq.heappop(counter)
    idx *= -1
    result += (curr_i * num)
    print(curr_i, num, result, w, idx)
    curr_i += 1

print(result)




