from collections import deque
N, M, K = map(int, input().split())
trees = []
die_trees = []
A = []
land = [[5] * N for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
trees = []

def spring():
    next_trees = deque()
    for tree in trees:
        x, y, z = tree
        if land[x][y] >= z: # 양분섭취
            land[x][y] -= z
            next_trees.append([x, y, z + 1])
        else:
            die_trees.append([x, y, z])
    return next_trees

def summer():
    for tree in die_trees:
        x, y, z = tree
        land[x][y] += (z // 2)
    die_trees.clear()


def fall():
    baby_tree = []
    length = len(trees)
    for i in range(length):
        x, y, z = trees[i]
        if z % 5 == 0:
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                baby_tree.append([nx, ny, 1])
    for b in baby_tree:
        trees.appendleft(b)

def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    trees.append([x - 1, y - 1, z])

trees.sort()
trees = deque(trees)
for _ in range(K):
    trees = spring()
    summer()
    fall()
    winter()
    if not trees:
        break
print(len(trees))
