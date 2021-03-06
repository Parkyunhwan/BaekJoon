'''
    풀진 말고 한번 더 이해해보기
    https://sihyungyou.github.io/baekjoon-2293/

    dp[j] = dp[j] + dp[j - arr[i]]
    arr[i] 값 이전 동전으로 만든 j의 갯수 -> dp[j]
    arr[i] 값을 포함한 동전으로 만든 j의 갯수 -> dp[j - arr[i]]
'''
n, k = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (k + 1)


dp[0] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= arr[i]:
            dp[j] = dp[j] + dp[j - arr[i]]
print(dp[k])
