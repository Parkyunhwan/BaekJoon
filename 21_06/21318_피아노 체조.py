import sys
input = sys.stdin.readline
N = int(input())
arr = [0] + list(map(int, input().split()))

count = [0] * (N + 1)
for i in range(1, N + 1):
    if arr[i - 1] > arr[i]:
        count[i] = count[i - 1] + 1
    else:
        count[i] = count[i - 1]

for _ in range(int(input())):
    x, y = map(int, input().split())
    c = count[y] - count[x]
    print(c)
