N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
left, right = 0, 0
sm = 0
while left <= right and right <= N:
    if sm >= M:
        if sm == M:
            result += 1
        sm -= arr[left]
        left += 1
    else:
        if right == N:
            break
        sm += arr[right]
        right += 1


print(result)