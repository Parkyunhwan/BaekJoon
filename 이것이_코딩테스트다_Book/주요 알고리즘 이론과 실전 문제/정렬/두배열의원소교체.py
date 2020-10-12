n, k = map(int, input().split())
a = list(map(int, input().split())) # 가장 작은 3가지
b = list(map(int, input().split())) # 가장 작은 3가지
a.sort()
b.sort()

for i in range(k):
    #a[i] = b[n-1-i]
    a[i] = b[-(i+1)]
print(sum(a))
