print("문자열 두 개를 입력해주세요.")
arr1 = list(input())
arr2 = list(input())

dp = [[0] * (len(arr1) + 1) for _ in range(len(arr2) + 1)]

for i in range(1, len(arr2) + 1):
    for j in range(1, len(arr1) + 1):
        if arr2[i - 1] == arr1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

mx = 0
print(arr1)
for i, a in enumerate(dp):
    if i == 0:
        print('%', end=' ')
    else:
        print(arr2[i - 1], end=' ')
    mx = max(mx, max(a))
    print(a)

print("max length : %d" % mx)