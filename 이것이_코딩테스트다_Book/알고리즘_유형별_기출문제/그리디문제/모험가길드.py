# 1회차 => 35분
# 2회차 =>
n = int(input())
arr = list(map(int, input().split()))
check = 0
arr.sort()
print(arr)
i = 0
result = 0

while True:
    val = arr[i]
    if (i+1) - check == val:

        result += 1
        check += val
    i += 1
    if i >= len(arr):
        break
print(result)