n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sm = 0
curr = 0
for val in arr:
    curr += val
    sm += curr
print(sm)