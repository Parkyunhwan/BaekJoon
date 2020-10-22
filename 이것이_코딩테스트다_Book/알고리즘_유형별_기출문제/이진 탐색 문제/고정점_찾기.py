n = int(input())
arr = list(map(int, input().split()))
start = 0
end = len(arr)-1

# start <= end 이면 end입력시 len-1, start < end 이면 end입력시 len
while start <= end:
    mid = (start + end) // 2
    print(start, end, mid)
    if arr[mid] == mid:
        print(mid)
        exit(0)
    elif arr[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
print(-1)
