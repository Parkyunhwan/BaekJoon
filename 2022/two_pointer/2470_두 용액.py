import sys
N = int(input())
values = list(map(int, input().split()))
values.sort()

result_val = sys.maxsize
result = []

left, right = 0, len(values) - 1
while left < right:
    sum_value = values[left] + values[right]
    if result_val > abs(sum_value):
        result = [values[left], values[right]]
        result_val = abs(sum_value)

    if sum_value == 0:
        result = [values[left], values[right]]
        break
    elif sum_value > 0:
        right -= 1
    else:
        left += 1

print(*result)
