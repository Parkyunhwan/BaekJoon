def dfs(index):
    global mn

    if index == (n // 2):
        startS = 0
        linkS = 0

        for i in range(n):
            if i not in start:
                link.append(i)
        for i in range(n // 2 - 1):
            for j in range(i + 1, n // 2):
                startS += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                linkS += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        diff = abs(startS - linkS)
        mn = min(mn, diff)
        link.clear()

        return

    for i in range(n):
        if i in start:
            continue
        if len(start) > 0 and start[len(start) - 1] > i: # 중복제거
            continue
        start.append(i)
        dfs(index + 1)
        start.pop()

n = int(input())

arr = []
start = []
link = []

for i in range(n):
    arr.append(list(map(int, input().split())))

mn = 1e9
dfs(0)
print(mn)