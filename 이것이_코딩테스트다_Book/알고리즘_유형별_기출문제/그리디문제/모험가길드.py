# 2회차 => O (더 안해도 됨)
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
count = 0
for i in range(len(arr)):
    val = arr[i]
    count += 1
    if val == count:
        result += 1
        count = 0
print(result)
# 1회차 => 35분
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
