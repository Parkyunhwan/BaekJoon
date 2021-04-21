'''
    파이썬은 동적으로 배열크기를 할당하기에

    1과 2인 경우에 따로 처리를 해줘야하는 문제가 발생할 수 있다. 물론 첨부터 최대 크기를 잡고 시작하면 발생 x

'''
n = int(input())
arr = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = int(input())

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1]
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

    print(dp[n])