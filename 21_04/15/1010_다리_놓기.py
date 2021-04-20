'''
    http://blog.naver.com/PostView.nhn?blogId=occidere&logNo=220876138317&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=false&from=postView
'''
for _ in range(int(input())):
    N, M = map(int, input().split())

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, M + 1):
        dp[1][i] = i

    for i in range(2, N + 1):
        for j in range(i, M + 1):
            for k in range(j, i - 1, -1):
                dp[i][j] = dp[i][j] + dp[i - 1][k - 1]

    print(dp[N][M])
