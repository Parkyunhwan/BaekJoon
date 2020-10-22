n, x = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = len(arr)
pivot = -1
while start < end:
    mid = (start + end) // 2
    if arr[mid] == x:
        pivot = mid
        break
    elif arr[mid] > x:
        end = mid - 1
    else:
        start = mid + 1

if pivot == -1:
    print(-1)
    exit(0)
count = 0
for i in range(pivot,-1,-1):
    if arr[i] == x:
        count +=1
    else:
        break
for i in range(pivot+1,len(arr)):
    if arr[i] == x:
        count +=1

print(count)
