print("문자열 두 개를 입력해주세요.")
arr1 = list(input())
arr2 = list(input())

dp = [[0] * (len(arr1) + 1) for _ in range(len(arr2) + 1)]

for i in range(1, len(arr2) + 1):
    for j in range(1, len(arr1) + 1):
        if arr2[i - 1] == arr1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

st = []

len1 = len(arr1)
len2 = len(arr2)
print(dp[len2][len1])
while dp[len2][len1] != 0:
    if dp[len2][len1] == dp[len2][len1 - 1]:
        len1 -= 1
    elif dp[len2][len1] == dp[len2 - 1][len1]:
        len2 -= 1
    else:
        st.append(arr2[len2 - 1])
        len1 -= 1
        len2 -= 1

while st:
    print(st.pop(), end='')
