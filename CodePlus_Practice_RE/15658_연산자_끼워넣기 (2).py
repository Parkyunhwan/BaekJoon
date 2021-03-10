import sys
n = int(input())
arr = list(map(int, input().split()))

oper = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(plus, minus, mul, div, index, sum_value):
    global mx, mn
    if index == n:
        mx = max(mx, sum_value)
        mn = min(mn, sum_value)
        return

    if plus > 0:
        dfs(plus - 1, minus, mul, div, index + 1, sum_value + arr[index])
    if minus > 0:
        dfs(plus, minus - 1, mul, div, index + 1, sum_value - arr[index])
    if mul > 0:
        dfs(plus, minus, mul - 1, div, index + 1, sum_value * arr[index])
    if div > 0:
        dfs(plus, minus, mul, div - 1, index + 1,
            -1 * (-sum_value // arr[index]) if sum_value < 0 < arr[index] else sum_value // arr[index])


dfs(oper[0], oper[1], oper[2], oper[3], 1, arr[0])

print("{0}\n{1}".format(mx, mn))

