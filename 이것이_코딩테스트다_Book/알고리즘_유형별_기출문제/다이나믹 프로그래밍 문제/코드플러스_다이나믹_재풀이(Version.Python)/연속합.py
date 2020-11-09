# -1001 을 하거나 가장 작은수를 구하거나..
# 숫자가 연속되므로 구하기 쉽다.
n = int(input())
arr = [0] + list(map(int, input().split()))
mn = min(arr)
d = [mn] * (n+1)

for i in range(1, n+1):
        d[i] = max(arr[i], arr[i] + d[i-1])

print(max(d))


# n = int(input())
# num_list = list(map(int, input().split()))
# temp = [0 for _ in range(n)]
# result = -1001
#
# for i in range(n):
#     temp[i] = max(temp[i - 1] + num_list[i], num_list[i])
#     result = max(result, temp[i])
#
# print(result)

