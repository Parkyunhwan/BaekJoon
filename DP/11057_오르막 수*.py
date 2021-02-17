n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    dp[i][0] = sum(dp[i - 1])
    dp[i][9] = dp[i - 1][9]
    for j in range(1, 9):
        dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]

print(sum(dp[n]) % 10007)


# review this code
# 1차원 배열 재사용으로 품
# 또한 점진적으로 더해가며 답을 구함.
import sys
N = int(sys.stdin.readline())
nums = [1] * 10
mod = 10007
for _ in range(N-1):
    for i in range(1, 10):
        nums[i] = (nums[i] + nums[i-1]) % mod
sys.stdout.write(str(sum(nums) % mod))

#출처: https://suri78.tistory.com/92 [공부노트]