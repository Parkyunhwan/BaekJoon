n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
P = [0]*(n+1)
mx = -1


def backtrace(idx, num):
    if idx == 0:
        return
    if dp[idx] == num: # 뒤에서부터 검사
        backtrace(idx-1, num-1) # 찾는 값이라면 다음 값 뒤에서부터 검사
        print(a[idx], end=" ")
    else:
        backtrace(idx-1, num) # 찾는 위치가 아니라면 그 전값 검사


for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    mx = max(mx, dp[i]) # => 이 부분이 꼭 필요하다.
    # 왜냐하면 꼭 마지막 원소가 최대길이를 가지지 않는다. 따라서 원소중 최대길이를 구해야한다.
print(mx)
backtrace(len(dp)-1, mx)
# lst = []
# for i in range(n, 0, -1):
#     if mx == dp[i]:
#         mx -= 1
#         lst.append(a[i])
# lst.reverse()
# for i in lst:
#     print(i, end=" ")
