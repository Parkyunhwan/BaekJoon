n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = right = count = sm = 0
while left != n:
    if sm < 0 and right != n:
        sm += arr[right]
        right += 1
    else:
        sm -= arr[left]
        left += 1
    if sm == m:
        count += 1
print(count)