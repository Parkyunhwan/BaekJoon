# 그냥 푼 것
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))


def solve():
    count = 0
    for i in range(n):
        sm = 0
        for j in range(i, n):
            sm += arr[j]
            if sm == m:
                count += 1
                break
            elif sm > m:
                break
    return count


print(solve())

## 투 포인터 해결법 https://rebas.kr/765
n, m = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    left = right = ans = s = 0
    while True:
        if s >= m:
            s -= a[left]
            left += 1
        else:
            if right == n:
                break
            s += a[right]
            right += 1
        if s == m:
            ans += 1
    return ans

print(solve())
