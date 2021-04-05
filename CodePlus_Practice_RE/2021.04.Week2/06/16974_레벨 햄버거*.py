'''
    https://nim-code.tistory.com/268
    블로그 보고 이런 방식이 있다고 생각하고 넘어가자.
'''
N, X = map(int, input().split())

burger = [0] * (N + 1)
patty = [0] * (N + 1)
burger[0] = 1
patty[0] = 1

def getPatty(n, x):

    if n == 0 and x == 1:
        return 1
    if n == 0 and x == 0:
        return 0

    if x == 1:
        return 0

    elif x <= burger[n - 1] + 1:
        return getPatty(n - 1, x - 1)
    elif x == 1 + burger[n - 1] + 1:
        return patty[n - 1] + 1

    elif x <= burger[n - 1] + 1 + burger[n - 1] + 1:
        return patty[n - 1] + 1 + getPatty(n - 1, x - 1 - burger[n - 1] - 1)

    else:
        return patty[n - 1] * 2 + 1

for i in range(1, N + 1):
    burger[i] = 1 + burger[i - 1] + 1 + burger[i - 1] + 1
    patty[i] = patty[i - 1] + 1 + patty[i - 1]
print(getPatty(N, X))