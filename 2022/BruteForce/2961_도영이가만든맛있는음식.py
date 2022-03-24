import sys
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

min_result = sys.maxsize
def dfs(idx, sour_sum, bitter_sum):
    global min_result
    if idx == N:
        if bitter_sum > 0:
            diff = abs(sour_sum - bitter_sum)
            min_result = min(diff, min_result)
            return
        else:
            return

    dfs(idx + 1, sour_sum, bitter_sum)
    dfs(idx + 1, sour_sum * arr[idx][0], bitter_sum + arr[idx][1])

dfs(0, 1, 0)
print(min_result)