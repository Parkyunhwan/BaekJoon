'''
    아예 손도 못댐 (다시 풀기)

    ---
    즉 이진 트리를 만드는 모든 방법에 대해 최소 비용을 계산해야 한다.

    풀이 1으로 공부해봄..
    일단, 하나만 기억하자 -> dp[i][j]는 i부터 j까지 합치는 값의 최소 비용을 저장한다.

    다음 번엔 좀더 효율적인 풀이 2를 공부하자.
    https://js1jj2sk3.tistory.com/3

    풀이 2:
    가장 넓은 범위 경우부터 따져나가는 방법

    하나의 경우를 -> 왼쪽 최송비용, 오른쪽 최소비용의 합으로 나눠서 가져가는 것

    미드를 기준으로 왼, 오른으로 나눠 재귀적으로 수행함.
    for (int mid = tx; mid < ty; ++mid) {
        int left = dpf(tx, mid);
        int right = dpf(mid + 1, ty);
        dp[tx][ty] = min(dp[tx][ty], left + right);
    }
'''

'''
    하향식 방법이므로 작은 값부터 천천히 구해나가야 한다.
    우리가 구해야하는 것은 1 ~ n까지 모두 합친 최소값이다.
    따라서, 가장 작은 단위는 2개를 합치는 경우이다.
    2개를 합치는 경우를 먼저 구하고 다음에 3개, 4개 ... n개 까지 확장해나가도록 하자.
'''
'''
for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    psum = [0] * (n + 1)

    sm = 0
    for i in range(1, n + 1):
        sm += arr[i]
        psum[i] = sm

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for gap in range(1, n + 1):
        for start in range(1, n + 1):
            end = start + gap
            if end > n:
                break
            dp[start][end] = 1e9
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + (psum[end] - psum[start - 1]))

    mx = 0
    for row in dp:
        mx = max(mx, max(row))
    print(mx)
'''
'''
    방법 2
'''
for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    psum = [0] * (n + 1)

    sm = 0
    for i in range(1, n + 1):
        sm += arr[i]
        psum[i] = sm

    dp = [[1e9] * (n + 1) for _ in range(n + 1)]

    def dp_rec(s, e):
        if dp[s][e] != 1e9:
            return dp[s][e]

        if s == e:
            dp[s][e] = 0
            return 0

        for mid in range(s, e):
            ret1 = dp_rec(s, mid)
            ret2 = dp_rec(mid + 1, e)
            dp[s][e] = min(dp[s][e], ret1 + ret2 + (psum[e] - psum[s - 1]))
        return dp[s][e]
    print(dp_rec(1, n))