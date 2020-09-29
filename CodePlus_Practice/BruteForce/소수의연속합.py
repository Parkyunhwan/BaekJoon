# 루트 n 까지만 나누어서 떨어지면 소수가 아니다. (루트 또는 제곱을 하는 이유)
# 에라토스테네스 + 투 포인터 문제

n = int(input())
ch = [False]*(n+1)
pn = []


def solve():
    sm, count, left, right = 0, 0, 0, 0
    while True:
        if sm >= n:
            sm -= pn[left]
            left += 1
        else:
            if right == len(pn):
                break
            sm += pn[right]
            right += 1
        if sm == n:
            count += 1
    return count


def erato():
    global ch
    for i in range(2, n+1):
        if i*i > n:
            break
        if ch[i] is False:
            k = 2
            m = k*i
            while m <= n:
                ch[m] = True
                k += 1
                m = k*i
    for t in range(2, n + 1):
        if ch[t] is False:
            pn.append(t)


erato()
print(solve())