n = int(input())
a = [0] + list(map(int, input().split()))
df = [1] * (n+1)
dr = [1] * (n+1)
for i in range(1, n+1):
    for j in range(1, i):
        if a[i] > a[j]:
            df[i] = max(df[i], df[j]+1)

for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        if a[i] > a[j]:
            dr[i] = max(dr[i], dr[j]+1)

for i in range(1, n+1):
    df[i] = df[i] + dr[i]

print(max(df)-1)
