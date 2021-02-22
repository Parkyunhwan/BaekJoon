k, n = map(int, input().split())

arr = [int(input()) for _ in range(k)]

pivot = max(arr) // 2


result = 0
left = 1
right = max(arr)

while left <= right:
    pivot = (left + right) // 2
    count = 0
    for val in arr:
        count += val // pivot

    if count >= n: # 더 큰 값 도전
        result = max(result, pivot)
        left = pivot + 1
    else:
        right = pivot - 1
print(result)