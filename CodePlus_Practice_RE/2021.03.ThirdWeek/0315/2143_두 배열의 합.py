from collections import defaultdict
t = int(input())
n = int(input())
arr_a = list(map(int, input().split()))
m = int(input())
arr_b = list(map(int, input().split()))

dict_a, dict_b = defaultdict(int), defaultdict(int)
for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += arr_a[j]
        dict_a[sm] += 1

for i in range(m):
    sm = 0
    for j in range(i, m):
        sm += arr_b[j]
        dict_b[sm] += 1

result = 0
for val in dict_a:
    if dict_b[t - val]:
        result += (dict_b[t - val] * dict_a[val])

print(result)