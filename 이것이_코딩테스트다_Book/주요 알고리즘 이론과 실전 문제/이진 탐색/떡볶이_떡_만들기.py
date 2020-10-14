# 이진탐색을 통해 M보다 큰 수에서 M을 뺀 값을 더한다
# 배열의 길이가 아닌 떡볶이의 최대 길이를 기준으로 이진 탐색을 진행해야만 한다.
# 떡볶이의 양에 따라서 자를 위치가 결정되기 때문에 반복문을 통한 구현이 편하다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2  #  떡 길이의 중간을 설정 -> array 갯수의 중간이 아님
    for x in arr:
        if x > mid:
            total += x - mid

    if total >= m:  # 자른 떡이 목표보다 클 때 높이를 더 높여도됨
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)