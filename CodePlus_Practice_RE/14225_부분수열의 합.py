import itertools
n = int(input())

arr = list(map(int, input().split()))

answer = 0
result = [False] * 2000000
def dfs(index, sum_value):
    global answer

    if index == n:
        result[sum_value] = True
        return
    dfs(index + 1, sum_value)
    dfs(index + 1, sum_value + arr[index])


dfs(0, 0)

for i in range(2000000):
    if not result[i]:
        print(i)
        break