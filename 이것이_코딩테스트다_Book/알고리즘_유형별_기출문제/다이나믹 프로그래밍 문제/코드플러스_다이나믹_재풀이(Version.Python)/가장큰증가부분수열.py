# 나보다 작은거에서 나를 더한 것중 가장 큰값을 나한테 더한다.
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
result = 0
for i in range(1, n + 1):
    d[i] = a[i] # dp에 대한 초기화가 필요하다. 나 자신만으로 전에 증가했던 값보다 클수가 있다.
    for j in range(1, i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + a[i])
print(max(d))
