import bisect

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
result = [0] * m
arr_n.sort()

for i, val in enumerate(arr_m):
    left = bisect.bisect_left(arr_n, val)
    right = bisect.bisect_right(arr_n, val)

    result[i] = right - left

for v in result:
    print(v, end=' ')
