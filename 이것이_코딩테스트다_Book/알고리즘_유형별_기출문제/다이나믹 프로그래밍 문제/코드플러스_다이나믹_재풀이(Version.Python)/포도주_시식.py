# n = int(input())
# arr = [0] + [int(input()) for _ in range(n)] + [0]
#
# d = [0]*(n+2)
# d[1], d[2] = arr[1], arr[1]+arr[2]
# for i in range(3, n+1):
#     d[i] = d[i-1]  # 선택안하는 경우를 포함시켜버림.. ㄷㄷ
#     d[i] = max(d[i], d[i-2]+arr[i])
#     d[i] = max(d[i], d[i-3]+arr[i-1]+arr[i])
#
# print(d[n])
#
#
# # 2회차 실패 -> 현재 자신을 선택안하는 경우를 생각하지 못했다. 너무 어려운 생각인것같다.
# n = int(input())
# arr = [0] + [int(input()) for _ in range(n)]
# d = [0]*(n+2)
# d[1] = arr[1]
# d[2] = arr[1] + arr[2]
#
# for i in range(3, n+1):
#     d[i] = d[i-1]
#     d[i] = max(arr[i] + d[i-2], arr[i] + arr[i-1] + d[i-3])
#
# print(d[n])

n = int(input())

arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 1])
print(max(dp))