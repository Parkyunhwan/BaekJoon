# 이진탐색을 통해 M보다 큰 수에서 M을 뺀 값을 더한다
n, m = int(input().split())
arr = list(int(input().split()))
arr.sort(reverse=True)

mn = float("INF")
mid = len(arr) // 2
tr = arr[mid:]
tl = arr[:mid]
sm = 0
for t in tr:
    if t - m >= 0:
        sm += (t - m)
mn = min(mn, sm)
