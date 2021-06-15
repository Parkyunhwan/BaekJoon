arr = input().split('-')

for i, a in enumerate(arr):
    sm = 0
    if len(a.split('+')) > 0:
        a = a.split('+')
        for val in a:
            sm += int(val)
    arr[i] = sm

result = int(arr[0])
for i in range(1, len(arr)):
    val = int(arr[i])
    result -= val

print(result)