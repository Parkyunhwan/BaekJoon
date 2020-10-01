# https://suri78.tistory.com/171
# 딕셔너리를 이용한 방법

T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

acm, bcm = {}, {}
for i in range(n):
    t = 0
    for j in range(i, n):
        t += a[j]
        if acm.get(t):  # 존재여부 확인
            acm[t] += 1
        else:
            acm[t] = 1

for i in range(m):
    t = 0
    for j in range(i, m):
        t += b[j]
        if bcm.get(t):
            bcm[t] += 1
        else:
            bcm[t] = 1

ans = 0
for i in acm:
    if bcm.get(T-i):
        ans += (acm[i]*bcm[T-i])  # 각자의 갯수를 세었으므로 서로 곱해줘야한다.( A -> 3이되는 합 2개 (1,2),(1,1,1) B -> 4가되는 합 (2, 2), (1,1,
        # 2) 조합 => 4개)
print(ans)

# bisect를 이용한 방법
import bisect

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_sum, b_sum = [], []

for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        a_sum.append(sm)

for i in range(m):
    sm = 0
    for j in range(i, m):
        sm += b[j]
        b_sum.append(sm)

#  시간 초과 --> 어떻게 하면 각자의 합을 O(n^3)보다 빠른 속도로 구할 수 있을까??
# for k in range(m):
#     for i in range(k, m):
#         sm = 0
#         for j in range(k, i+1):
#             sm += b[j]
#         b_sum.append(sm)

# -> bisect를 이용하여 합에서 차를 이용해 1000번만에 답을 구할 수 있다.
b_sum.sort()
count = 0
for a in a_sum:
    upper = bisect.bisect_right(b_sum, t - a)
    lower = bisect.bisect_left(b_sum, t - a)
    count += (upper - lower)
print(count)

# ( (1001+1) * 500 )^2 -> 500억 연산 ..
# for na in a_sum:
#     for nb in b_sum:
#         if na+nb == t:
#             count += 1
