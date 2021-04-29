N, M = map(int, input().split())
namu = list(map(int, input().split()))

max_size = max(namu)
left = 0
right = max_size

ret = 0
while left <= right:
    mid = (left + right) // 2
    sm = 0
    for val in namu:
        if val > mid:
            sm += (val - mid)
    if sm >= M:
        left = mid + 1
        ret = mid
    else:
        right = mid - 1

print(ret)