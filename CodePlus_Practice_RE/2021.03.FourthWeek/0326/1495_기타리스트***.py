'''
    이진트리로 쪼개지는 dp
    https://jaimemin.tistory.com/473 (상향식)
    https://yabmoons.tistory.com/547 (하향식)
'''
n, s, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

# dp = [[False] * (m + 1) for _ in range(n + 1)]
# dp[0][s] = True
#
# for i in range(1, n + 1):
#     for j in range(0, m + 1):
#         if dp[i - 1][j]:
#             if j - arr[i] >= 0:
#                 dp[i][j - arr[i]] = True
#             if j + arr[i] <= m:
#                 dp[i][j + arr[i]] = True
#
# for j in range(m, -1, -1):
#     if dp[n][j]:
#         print(j)
#         exit(0)
# print(-1)


dp = [[-1] * (m + 1) for _ in range(n + 1)]


def get_value(idx, volume):
    if volume < 0 or volume > m:
        return -100

    if idx == n:
        return volume

    if dp[idx][volume] != -1:
        return volume

    dp[idx][volume] = max(get_value(idx + 1, volume + arr[idx + 1]), get_value(idx + 1, volume - arr[idx + 1]))
    return dp[idx][volume]

result = get_value(0, s)
if result == -100:
    print(-1)
else:
    print(result)
