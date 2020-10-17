arr = list(input())
arr = [int(i) for i in arr]
prev = arr[0]
count = [0]*2

for a in arr:
    if prev != a:
        count[prev] += 1
    prev = a
count[prev] += 1
print(min(count[0], count[1]))