''# coding=utf-8
# 내가 생각을 성공한 부분
# => 현재까지 연속 한잔 째 마신 경우
# => 현재까지 연속 2잔 째 마신 경우

# 생각하지 못한 경우
# => 현재 잔을 안 마시는 경우!!
# 999 999 1 1 999 999 (현재 잔을 안 마셔야 최대가 되는 경우가 존재한다!!)

n = int(input())
arr = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n + 1)]

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])
if n >= 3:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])
        dp[i] = max(dp[i], dp[i - 1])
    print(max(dp))