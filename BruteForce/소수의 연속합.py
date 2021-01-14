n = int(input())
arr = [False] * (n + 1)
val = []
count = 0
if n == 1:
    print(0)
    exit(0)

if n > 1:
    for i in range(2, n + 1):
        j = 2
        while i * j <= n:
            arr[i * j] = True
            j += 1

    for i in range(2, n + 1):
        if not arr[i]:
            val.append(i)

    left = right = sm = 0
    length = len(val)
    while True:
        if sm >= n:
            sm -= val[left]
            left += 1
        elif sm < n:
            if right == length:
                break
            sm += val[right]
            right += 1

        if sm == n:
            count += 1
    print(count)
