import sys
r, c = map(int,sys.stdin.readline().split())
arr = [list(map(lambda x: ord(x) - ord('A'), sys.stdin.readline().strip())) for _ in range(r)]

print(arr)
mx = -1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, index):
    global mx
    mx = max(index, mx)

    for k in range(4):
        tx = x + dx[k]; ty = y + dy[k]
        if 0 <= tx < c and 0 <= ty < r:
            tmp = arr[ty][tx]
            if ch[tmp] == 0:
                #print(arr[ty][tx])
                ch[tmp] = 1
                dfs(tx, ty, index+1)
                ch[tmp] = 0

ch = [0]*(r*c)

ch[arr[0][0]] = 1
dfs(0, 0, 1)
print(mx)