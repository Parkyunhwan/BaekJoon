import bisect

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

count = 0

# 시간 초과... 굳이 O(nlogn)
# while k != 0:
#     index = bisect.bisect_right(arr, k) - 1
#     k -= arr[index]
#     count += 1

# O(n)
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if arr[i] > k: # 동전금액보다 큰 값일 땐 더 작은 값을 찾는다.
        continue
    count += (k // arr[i]) # 현재 동전이 들어갈 수 있는 갯수를 더한다.
    k %= arr[i] # 남은 잔액을 계산한다.
print(count)
