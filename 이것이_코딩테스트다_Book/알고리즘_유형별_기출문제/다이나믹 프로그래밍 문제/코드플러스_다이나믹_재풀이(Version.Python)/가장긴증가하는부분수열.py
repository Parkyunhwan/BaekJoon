# 뭔소리여 재풀이..
n = int(input())
arr =[0] + list(map(int, input().split()))
d = [0]*(n+1)


mx = 0
for i in range(1, n+1):
    mn = 0
    for j in range(0, i):
        if arr[i] > arr[j]:
            if mn < d[j]:
                mn = d[j]
    d[i] = mn + 1
    if mx < d[i]:
        mx = d[i]

print(mx)