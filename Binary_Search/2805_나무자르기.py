import sys
n, m = map(int, input().split())

arr = list(map(int, input().split()))

mx = max(arr)

left = 0
result = 0
right = mx
while left <= right:
    mid = (left + right) // 2
    meters = 0
    for val in arr:
        if val > mid:
            meters += (val - mid)
    if meters >= m:
        left = mid + 1
        result = max(result, mid)
    else:
        right = mid - 1
print(result)