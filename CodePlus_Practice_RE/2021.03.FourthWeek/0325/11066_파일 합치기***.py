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
import sys
for _ in range(int(input())):
    k = int(input())
    arr = [0] + list(map(int, input().split()))

    psum = [[0] * (k + 1) for _ in range(k + 1)]
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        sm = 0
        for j in range(i, k + 1):
            sm += arr[j]
            psum[i][j] = sm

    for row in psum:
        print(row)

    for gap in range(1, k + 1):

        for start in range(1, k + 1):
            end = start + gap
            if end == k + 1:
                break
            dp[start][end] = sys.maxsize
            for i in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][i] + dp[i + 1][end] + psum[start][end])

    print(dp[1][k])
