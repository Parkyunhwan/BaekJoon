N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sum_arr = [0] * (N + 1)
sm = 0
for i, val in enumerate(arr):
    sm += val
    sum_arr[i] = sm

left = 0
right = 1
sm = 0
answer = 1e9
while left < N + 1:
    sm = sum_arr[right] - sum_arr[left]
    if sm < S:
        right += 1
        if right == N + 1:
            break
    elif sm >= S:
        if answer > right - left:
            answer = right - left
        left += 1

if answer == 1e9:
    print(0)
else:
    print(answer)