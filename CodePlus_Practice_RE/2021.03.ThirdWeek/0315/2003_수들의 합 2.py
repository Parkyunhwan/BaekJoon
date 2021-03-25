# 투 포인터로 풀 수 있었다.
# 탈출 조건이 정확해야 했던 문제 (앞으로 더 늘어날 수 없다면 합이 m이하일 때 빠져나오면 된다.)

n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = right = 0
sm = 0
count = 0
while left < n:
    if sm < m and right < n:
        sm += arr[right]
        right += 1
    else:
        sm -= arr[left]
        left += 1

    if sm == m:
        count += 1

print(count)