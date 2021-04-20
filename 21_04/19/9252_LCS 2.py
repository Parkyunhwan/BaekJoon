A = list(input())
B = list(input())

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

len_A = len(A)
len_B = len(B)

prev = dp[len(A)][len(B)]
st = []

print(dp[len_A][len_B])

while dp[len_A][len_B] != 0:
    while dp[len_A][len_B] == dp[len_A][len_B - 1]:
        len_B -= 1
    while dp[len_A][len_B] == dp[len_A - 1][len_B]:
        len_A -= 1
    st.append(A[len_A - 1])
    len_A -= 1
    len_B -= 1

for i in range(len(st) - 1, -1, -1):
    print(st[i], end='')


