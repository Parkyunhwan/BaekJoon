n, m = map(int, input().split())
ball = list(map(int, input().split()))
num = []
for i in range(m, 0, -1):
    num.append(ball.count(i))

s = 0
for i in range(len(num)):
    for j in range(i+1, len(num)):
        s += num[i] * num[j]
print(s)