n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(len(arr)):
    dp[i] = arr[i]

sm = 0
for i in range(1, len(arr)):
    if dp[i - 1] < 0:
        dp[i] = arr[i]
    else:
        dp[i] = dp[i - 1] + arr[i]
print(max(dp[1:]))


### 모범답안 만 보기
# dp 적인 풀이
# 1. 초기화는 최솟값으로
# 2. 현재값과 현재값을 더한 값을 비교해 더 큰 값을 넣는다. (현재 값보다 전체가 작으면 현재값부터 다시 시작)
n = int(input())
arr = [0] + list(map(int, input().split()))
mn = min(arr)
d = [mn] * (n+1)

for i in range(1, n+1):
        d[i] = max(arr[i], arr[i] + d[i-1])

print(max(d))