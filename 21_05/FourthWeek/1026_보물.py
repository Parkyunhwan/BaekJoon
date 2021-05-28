N = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(len(arr)):
    if i == 0:
        arr[i] = sorted(arr[i])
    else:
        arr[i] = sorted(arr[i], reverse=True)
sm = 0
for j in range(len(arr[0])):
    sm += (arr[0][j] * arr[1][j])

print(sm)