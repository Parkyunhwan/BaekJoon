n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
max_weight = 0

weight = 0
for i, val in enumerate(arr):
    max_weight = max(max_weight, val * (i + 1))
print(max_weight)