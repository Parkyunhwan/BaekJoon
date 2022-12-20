# 안될 땐 문제에 대한 조건을 찬찬히 침착하게 읽자
from itertools import permutations
from collections import defaultdict

N = int(input())
prices = [0] + list(map(int, input().split()))

# discount_info = [[0] for _ in range(N)]
discount_info = defaultdict(list)
idx = 1
i = 1
while i != N + 1:
    tmp = []
    for _ in range(int(input())):
        discount_info[i].append(list(map(int, input().split())))
        idx += 1
    i += 1

li = [x for x in range(1, N + 1)]

perm = list(permutations(li, N))

def calculate(per, prices):
    count = 0
    for idx2 in per:
        count += prices[idx2]
        if discount_info[idx2]:
            for discount in discount_info[idx2]:
                a, d = discount
                if prices[a] - d <= 0:
                    prices[a] = 1
                else:
                    prices[a] -= d
    return count


total_count = 0
min_count = sum(prices)
for per in perm:
    tmp = prices[:]
    total_count = calculate(per, tmp)
    min_count = min(min_count, total_count)

print(min_count)
