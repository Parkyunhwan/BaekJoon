n = int(input())
d = [[0]*11 for _ in range(n+1)]

for i in range(0, 10):
    d[1][i] = 1

for i in range(2, n+1):
    sm = 0
    for j in range(10):
        sm = (sm + d[i-1][j]) % 10007
        d[i][j] = sm

print(sum(d[n])%10007)