from collections import defaultdict
from itertools import combinations
n, s = map(int, input().split())

arr = list(map(int, input().split()))

mid = len(arr) // 2
arr_front = arr[:mid]
arr_back = arr[mid:]


front, back = defaultdict(int), defaultdict(int)
for i in range(len(arr_front) + 1):
    comb = combinations(arr_front, i)
    for com in list(comb):
        sm = sum(com)
        front[sm] += 1

for i in range(len(arr_back) + 1):
    comb = combinations(arr_back, i)
    for com in list(comb):
        sm = sum(com)
        back[sm] += 1

result = 0
for val in front:
    if back[s - val] > 0:
        result += (back[s - val] * front[val])

print(result-1 if s == 0 else result)