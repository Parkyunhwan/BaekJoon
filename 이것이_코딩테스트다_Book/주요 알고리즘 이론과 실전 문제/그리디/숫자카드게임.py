n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = -1
for com in arr:
    mn = min(com)
    mx = max(mx, mn)
print(mx)