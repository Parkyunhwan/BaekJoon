'''
    문제의 핵심 풀이
    N의 범위가 10만이 넘어가는데 어떻게 하면 이중포문을 쓰지 않고 특정범위에 있는 값을 검사할 수 있을까?

    *** 슬라이딩 윈도우 ***
    k개 까지는 슬라이딩 윈도우를 채운다. 이 때 먹은 sushi갯수를 종류별로 계산해둔다.
    먹은 종류의 수는 처음 먹을 때만 계산된다.

    k이상 부터는 앞에 스시를 빼고 새롭게 스시를 넣어주는데 이 때 sushi갯수가 0이되면 먹은 종류도 하나 빼주고 새롭게 먹은 것이 새로운 스시라면 +1

    -> 쿠폰의 초밥을 먹지 않았다면 +1해서 계산하고 아니라면 그냥 계산
'''
from collections import deque
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
sushi = [0] * (d + 1)

q = deque()
count = 0
result = 0
for i in range(N + k):
    i = i % N
    if len(q) < k:
        q.append(arr[i])
        if sushi[arr[i]] == 0:
            count += 1
        sushi[arr[i]] += 1

    elif len(q) == k:
        if sushi[c] == 0:
            result = max(result, count + 1)
        else:
            result = max(result, count)
        pop_value = q.popleft()
        sushi[pop_value] -= 1
        if sushi[pop_value] == 0:
            count -= 1
        q.append(arr[i])
        if sushi[arr[i]] == 0:
            count += 1
        sushi[arr[i]] += 1

print(result)