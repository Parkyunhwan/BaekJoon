n = int(input())

arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

if n <= 2:
    print(sum(arr))
    exit(0)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])
    # 2000 1000 10 30 2000 3000 이면 포도주를 2번연속 먹지 않는 경우가 생긴다.
    # 이를 방지하기 위해서 dp는 항상 최댓값을 유지하도록 한다.
    dp[i] = max(dp[i], dp[i - 1])
print(max(dp))
