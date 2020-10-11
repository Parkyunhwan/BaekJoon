# 이 문제의 그리디의 정당성은
# 문제 조건에서 k가 2이상이라고 했으므로 어떠한 경우에도 k로 나누는 것이 1로 빼는 것보다 빠르게 n을 줄일 수 있다.

n, k = map(int, input().split())
count = 0
while n != 1:
    if not n % k:
        n = n / k
    else:
        n = n - 1
    count += 1
print(count)