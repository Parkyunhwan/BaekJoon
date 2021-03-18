import sys
n = int(input())
arr = [0] + list(map(int, input().split()))

result = [sys.maxsize] * (n + 1)

result[1] = 0
for i in range(1, n + 1):
    jump_max = arr[i]
    for j in range(1, jump_max + 1):
        if i + j < n + 1:
            if result[i] + 1 < result[i + j]:
                result[i + j] = result[i] + 1

print(result[n]) if result[n] != sys.maxsize else print(-1)