n = int(input())
p = [0] + list(map(int, input().split()))
INF = int(1e9)
d = [INF] * (n+1)
for i in range(len(p)):
    d[i] = p[i]

for i in range(2, n+1):
    for j in range(1, i+1):
        d[i] = min(d[i], d[i-j] + p[j])

print(d[n])