n = int(input())
arr = [0] + [int(input()) for _ in range(n)] + [0]

d = [0]*(n+2)
d[1], d[2] = arr[1], arr[1]+arr[2]
for i in range(3, n+1):
    d[i] = d[i-1]  # 선택안하는 경우를 포함시켜버림.. ㄷㄷ
    d[i] = max(d[i], d[i-2]+arr[i])
    d[i] = max(d[i], d[i-3]+arr[i-1]+arr[i])

print(d[n])
