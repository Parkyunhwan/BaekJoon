N = int(input())
A = list(map(int, input().split()))

M = int(input())
arr = list(map(int, input().split()))

for val in arr:
    if val in A:
        print(1)
    else:
        print(0)