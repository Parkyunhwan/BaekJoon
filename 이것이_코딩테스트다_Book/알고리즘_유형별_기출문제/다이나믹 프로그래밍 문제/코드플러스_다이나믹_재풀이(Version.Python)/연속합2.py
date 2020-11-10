# 다이나믹 문제를 풀 때 선택해야 하는 경우가 생기면 차원을 나눠본다.

n = int(input())
arr = [0] + list(map(int, input().split()))

d = [[0, 0] for _ in range(n+1)]
mx = -1
for i in range(1, n+1):
    d[i][0] = max(arr[i], d[i-1][0] + arr[i])
    d[i][1] = max(d[i-1][0], d[i-1][1]+arr[i])
    mx = max(max(d[i]), mx)

print(mx)