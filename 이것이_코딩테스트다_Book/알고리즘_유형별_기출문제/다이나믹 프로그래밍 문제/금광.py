# -> 1회차 : 성공했지만 좀더 다이나믹하게 짜보자
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))

    dp = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(tmp[i*m+j])
        dp.append(temp)

    for j in range(1, m):
        dp[0][j] += max(dp[0][j-1], dp[1][j-1])
        dp[1][j] += max(dp[0][j-1], dp[1][j-1], dp[2][j-1])
        dp[2][j] += max(dp[1][j-1], dp[2][j-1])
    print(max(dp[0][m-1], dp[1][m-1], dp[2][m-1]))

# -> 좀 더 다이나믹하게 바꿔보자
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽위의 값을 계산
            if i == 0: # 자신이 0일때는 왼쪽위라는 값이 없으므로 0을 넣어준다.
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1: # 자신이 n-1 때는 왼쪽아래라는 값이 없으므로 0을 넣어준다.
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] += max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)