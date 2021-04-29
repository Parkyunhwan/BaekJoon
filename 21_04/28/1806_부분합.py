N, S = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0
sm = 0
min_length = 1e9
while left < N:
    if sm < S:
        if right == N:
            break
        sm += arr[right]
        right += 1
    else:
        min_length = min(min_length, right - left)
        sm -= arr[left]
        left += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)
