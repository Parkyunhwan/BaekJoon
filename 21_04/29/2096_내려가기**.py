import sys

read = sys.stdin.readline
arr = []

N = int(read())
for _ in range(N):
    arr.append(list(map(int, read().split())))

maxD = [[0 for _ in range(3)] for _ in range(N)]
minD = [[0 for _ in range(3)] for _ in range(N)]

maxD[0] = arr[0]
minD[0] = arr[0]

for i in range(1, N):
    maxD[i][0] = max(maxD[i - 1][0], maxD[i - 1][1]) + arr[i][0]
    minD[i][0] = min(minD[i - 1][0], minD[i - 1][1]) + arr[i][0]

    maxD[i][1] = max(maxD[i - 1][0], maxD[i - 1][1], maxD[i - 1][2]) + arr[i][1]
    minD[i][1] = min(minD[i - 1][0], minD[i - 1][1], minD[i - 1][2]) + arr[i][1]

    maxD[i][2] = max(maxD[i - 1][1], maxD[i - 1][2]) + arr[i][2]
    minD[i][2] = min(minD[i - 1][1], minD[i - 1][2]) + arr[i][2]

print(max(maxD[N - 1]), min(minD[N - 1]))
