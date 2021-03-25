'''
    못품 -> ...그냥 답이안나온다...어디가 틀렷는지 모르겟다...

'''


# n, m, k = map(int, input().split())
#
# A = [[0] * (n + 1)]
# for _ in range(n):
#     A.append([0] + list(map(int, input().split())))
# trees = []
# for row in A:
#     print(row)
# for _ in range(m):
#     trees.append(list(map(int, input().split())))
#
# arr = [[5] * (n + 1) for _ in range(n + 1)]
#
# def winter():
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             arr[i][j] += A[i][j]
#
# def spring(old_trees):
#     new_trees = []
#     die_trees = []
#     old_trees = sorted(old_trees, key=lambda x: x[2])
#     for old_tree in old_trees:
#         x, y, age = old_tree
#
#         if arr[x][y] < age:
#             die_trees.append([x, y, age])
#             continue
#         arr[x][y] = arr[x][y] - age
#         new_trees.append([x, y, age + 1])
#
#     return new_trees, die_trees
#
#
# def summer(die_trees):
#     for dt in die_trees:
#         x, y, age = dt
#         arr[x][y] += age // 2
#
#
# def fall(trees):
#     new_trees = []
#     for tree in trees:
#         x, y, age = tree
#         if age % 5 == 0:
#             for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
#                 nx, ny = x + dx, y + dy
#                 if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                     continue
#                 new_trees.append([nx, ny, 1])
#     return new_trees
#
# for _ in range(k):
#     ntrees, dtrees = spring(trees)
#     summer(dtrees)
#     ret = fall(ntrees)
#     ntrees.extend(ret)
#     trees = ntrees
#     winter()
#     print(trees)
#
# print(len(trees))
#
