arr = list(input())
arr = [int(a) for a in arr]
arr.sort(reverse=True)

sm = arr[0]
for i in range(1, len(arr)):
    if arr[i] != 0:
        sm *= arr[i]
print(sm)