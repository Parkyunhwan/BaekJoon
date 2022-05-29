import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))



def solve():
    left = 0
    right = 0
    sum_value = 0
    min_length = sys.maxsize
    while left < N:
        if sum_value < S:
            if right == N:
                break
            sum_value += arr[right]
            right += 1
        elif sum_value >= S:
            sum_value -= arr[left]
            min_length = min(min_length, right - left)
            left += 1
    return min_length

result = solve()
if result != sys.maxsize:
    print(result)
else:
    print(0)
