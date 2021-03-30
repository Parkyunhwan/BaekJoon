'''
    https://rebas.kr/844

'''

from collections import Counter
r, c, k = map(int, input().split())
arr = [[0] * 101 for _ in range(101)]

for i in range(1, 4):
    arr[i][1], arr[i][2], arr[i][3] = map(int, input().split())
n, m = 3, 3
for t in range(101):
    if arr[r][c] == k:
        print(t)
        exit(0)
    new_arr = []
    if n >= m:
        length = 0

        for i in range(1, n + 1):
            new_row = []
            row = arr[i]
            count = Counter(row)
            sorted_c = sorted(count.items(), key=lambda x:(x[1], x[0]))
            print(sorted_c)
            j = 1
            for val in sorted_c:
                if val[0] != 0:
                    arr[i][j], arr[i][j + 1] = val[0], val[1]
                j += 2

            m = max(m, (len(sorted_c) - 1) * 2)
    else:
        length = 0

        for j in range(1, m + 1):
            count = Counter()
            for i in range(1, n + 1):
                if arr[i][j] != 0:
                    count[arr[i][j]] += 1

            sorted_c = sorted(count.items(), key=lambda x: (x[1], x[0]))
            print(sorted_c)
            i = 1
            for val in sorted_c:
                if val[0] != 0:
                    arr[i][j], arr[i + 1][j] = val[0], val[1]
                i += 2

            n = max(n, len(sorted_c) * 2)
print(-1)