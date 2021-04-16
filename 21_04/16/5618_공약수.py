n = int(input())
arr = list(map(int, input().split()))

gong = 1

mn = min(arr)
for i in range(1, mn + 1):
    flag = True
    for val in arr:
        if val % i != 0:
            flag = False
            break
    if flag:
        print(i)
