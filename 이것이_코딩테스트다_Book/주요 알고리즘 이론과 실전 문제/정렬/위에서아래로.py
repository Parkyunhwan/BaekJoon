# 계수 정렬 풀이
n = int(input())
arr = [int(input()) for _ in range(n)]

check = [0] * (max(arr) + 1)
for com in arr:
    check[com] += 1

for i in range(len(check)):
    if check[i] >= 1:
        for j in range(check[i]):
            print(i, end=" ")
