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
''
import sys
for _ in range(int(input())):
    k = int(input())
    arr = [0] + list(map(int, input().split()))

    sm = [0] * (k + 1)
    for i in range(1, k + 1):
        sm[i] += sm[i - 1] + arr[i]

    dp = [[0] * (k + 1) for _ in range(k + 1)]
    # dp[i][j] 는 i부터 j까지 합치는 드는 최소 비용!

    for d in range(1, k):
        tx = 1
        while tx + d <= k:
            ty = tx + d
            dp[tx][ty] = sys.maxsize
            for mid in range(tx, ty):
                dp[tx][ty] = min(dp[tx][ty], dp[tx][mid] + dp[mid + 1][ty] + sm[ty] - sm[tx - 1])
            tx += 1

    print(dp[1][k])