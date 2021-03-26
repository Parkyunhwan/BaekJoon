n, k = map(int, input().split())

item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

item = [0] + item
dp = [0] * (k + 1)


def dps():
    for i in range(1, n + 1):
        for j in range(k, 0, - 1):
            if item[i][0] <= j:
                dp[j] = max(dp[j], dp[j - item[i][0]] + item[i][1])

dps()
print(dp[k])

