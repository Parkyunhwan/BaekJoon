'''
    부분 bfs와 dp를 섞은 문제

    탐색은 bfs로 값 계산은 dp로 했다.

'''

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

hap = [[0] * m for _ in range(n)]
hap[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        for dx, dy in (1, 0), (0, 1), (1, 1):
            ni, nj = i + dx, j + dy
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if hap[ni][nj] < hap[i][j] + arr[ni][nj]:
                hap[ni][nj] = hap[i][j] + arr[ni][nj]

print(hap[n - 1][m - 1])