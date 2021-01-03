import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

num_list = [0 for i in range(n)]
ans = sys.maxsize


def calculate():
    global ans
    s_sum, l_sum = 0, 0
    for i in range(n):
        for j in range(n):
            if num_list[i] and num_list[j]:
                s_sum += arr[i][j]
            elif not num_list[i] and not num_list[j]:
                l_sum += arr[i][j]
        ans = min(ans, abs(s_sum - l_sum))


def dfs(index):
    if sum(num_list) == n // 2:
        calculate()
    else:
        num_list[index] = 1
        dfs(index + 1)
        num_list[index] = 0


dfs(0)
print(ans)

