n = int(input())
arr = list(map(int, input().split()))

def recursion(i):
    if i < 0:
        return 0
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    return max(recursion(i-2) + arr[i], recursion(i-1))

d = [0] * n
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-2] + arr[i], d[i-1])
print(d[n-1])


# 탑다운 함수
def recursion(i):
    if i < 0:
        return 0
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    return max(recursion(i-2) + arr[i], recursion(i-1))