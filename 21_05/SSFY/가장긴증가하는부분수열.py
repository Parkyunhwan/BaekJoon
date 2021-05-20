print("길이와 배열값을 순서대로 입력하세요.")
x = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print("length : %d" % max(dp))