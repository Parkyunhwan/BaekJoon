'''
    에라토~~의 체를 사용하면 n이하의 모든 소수를 쉽게 구할 수 있다.
    2부터 n까지 모든 숫자에 대해 배숫값을 체크한다.
    배숫값에 체크 되지 않은 것들이 소수 값들이다.
'''
n = int(input())
ch = [False] * (n + 1)

def erato():
    global ch
    pn = []
    for i in range(2, n+1):
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
    return pn

primeList = erato()
sm = count = 0
left = right = 0
while left < len(primeList):
    if sm == n:
        count += 1
        sm -= primeList[left]
        left += 1
    elif sm < n:
        if right == len(primeList):
            break
        sm += primeList[right]
        right += 1
    else:
        sm -= primeList[left]
        left += 1

print(count)