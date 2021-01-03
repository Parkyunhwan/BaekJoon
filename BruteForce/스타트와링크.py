from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

num_list = list(range(n))

comb = combinations(num_list, n // 2) # 반으로 나누

res = float('inf')

for co in comb:
    start_mem = list(co)
    link_mem = list(set(num_list) - set(start_mem))

    start_two = list(combinations(start_mem, 2))
    link_two = list(combinations(link_mem, 2))

    start_sum = 0
    for x, y in start_two:
        start_sum += arr[x][y] + arr[y][x]

    link_sum = 0
    for x, y in link_two:
        link_sum += arr[x][y] + arr[y][x]

    res = min(res, abs(start_sum - link_sum))

print(res)

