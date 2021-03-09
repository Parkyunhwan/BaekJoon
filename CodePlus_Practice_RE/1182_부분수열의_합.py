import itertools
n, s = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
def dfs(arr, index, sum_value):
    global answer
    sum_value += arr[index]

    if sum_value == s:
        answer += 1

    if index == n - 1:
        return

    dfs(arr, index + 1, sum_value)
    dfs(arr, index + 1, sum_value - arr[index])

dfs(arr, 0, 0)
print(answer)