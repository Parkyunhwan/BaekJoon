N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

num = 0
for i in range(N - 1, -1, -1):
    val = arr[i]
    div, mod = divmod(K, val)
    if div > 0:
        num += div
        K = mod
    if mod == 0:
        break

print(num)