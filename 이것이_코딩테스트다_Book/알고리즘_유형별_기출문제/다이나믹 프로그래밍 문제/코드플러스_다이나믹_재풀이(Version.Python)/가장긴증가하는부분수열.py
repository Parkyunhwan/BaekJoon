# 1회차 -> 실패
# 2회차 -> 성공 ( O(n^2)의 시간복잡도 매 반복마다 첫원소부터 현재 원소전까지 가장 큰 증가하는 부분 수열을 구한다.
# 매 반복마다 그 중 가장 큰 최대 길이를 구해야한다.
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

mx = -1
for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    mx = max(mx, dp[i]) # => 이 부분이 꼭 필요하다.
    # 왜냐하면 꼭 마지막 원소가 최대길이를 가지지 않는다. 따라서 원소중 최대길이를 구해야한다.
print(mx)

# O(nlogn) 시간복잡도
# n번 반복과 반복마다 이진 탐색을 수행해서 올바른 순서 탐색
import bisect
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

L = []

for i in range(1, n+1):
    if not L or L[-1] < a[i]:
        L.append(a[i])
    else:
        L[bisect.bisect_left(L, a[i])] = a[i]

print(len(L))

##### O(NlogN)의 방법으로는 선택한 값들을 알수 없으므로 path방식을 통해 알아내도록 한다.
import bisect
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
P = [0]*(n+1)

L = []
def backtrace(idx, num):
    if idx == 0:
        return
    if P[idx] == num: # 뒤에서부터 검사
        backtrace(idx-1, num-1) # 찾는 값이라면 다음 값 뒤에서부터 검사
        print(a[idx])
    else:
        backtrace(idx-1, num) # 찾는 위치가 아니라면 그 전값 검사

for i in range(1, n+1):
    if not L or L[-1] < a[i]:
        L.append(a[i])
        P[i] = len(L)
    else:
        index = bisect.bisect_left(L, a[i])
        L[index] = a[i]
        P[i] = index+1

print(P)
print(L)
backtrace(n, len(L)) # 경로
print(len(L))