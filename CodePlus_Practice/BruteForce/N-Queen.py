## C의 알고리즘을 그대로 따라했지만 시간초과가 발생했다..

def promising(i):
    for j in range(i):
        if col[j] == col[i] or abs(col[i] - col[j]) == (i-j):
            return False
    return True

def N_queen(i):
    global result
    if i == n:
        result += 1
    else:
        for j in range(n):
            col[i] = j
            if promising(i):
                N_queen(i+1)

n = int(input())
col = [0 for _ in range(n)]
result = 0
N_queen(0)
print(result)


n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)

# https://wkdtjsgur100.github.io/N-Queen/ (백트래킹 문제는 python을 추천 안한다고 한다.
# 출처: https://rebas.kr/761 [PROJECT REBAS]