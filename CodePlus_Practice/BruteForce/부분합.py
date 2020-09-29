# 문제가 이상인지 같은 지 잘 읽고 확인하자.
#

import sys
n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


def solve():
    mn = 1e9
    k = sm = left = right = 0
    while right <= n:
        if sm >= m: # 경계값 분석이 필요하다. (True)도 가능
            mn = min(mn, k)
            sm -= arr[left]
            left += 1
            k -= 1
        else:
            if right == n:
                break
            sm += arr[right]
            right += 1
            k += 1
    if 1e9 != mn:
        return mn
    else:
        return 0


print(solve())
