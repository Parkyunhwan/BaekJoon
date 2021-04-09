'''
    이 문제가 복잡했던 이유는 벌꿀통을 뽑는데 dfs 하나
    뽑은 벌꿀 통에서 최댓값을 구하는 데 dfs 하나

    총 두개 의 dfs가 겹쳐서 나타나서 어려웠다.

    문제를 나눠서 보면 평이한데 두개를 겹쳐놔서 더 어려웠던 문제였다.
'''

from itertools import combinations


def get_max(bee_box):
    ret = []
    for box in bee_box:
        value = []
        for num in range(1, M + 1):
            combs = combinations(box, num)
            for com in list(combs):
                if sum(com) <= C:
                    summ = 0
                    for k in com:
                        summ += k ** 2

                    value.append(summ)
        ret.append(max(value))
    return sum(ret)


def select_map(idx, i, j, visited):
    global bee_box, mx

    if idx == 2:

        mx = max(get_max(bee_box), mx)
        return

    for ni in range(N):
        for nj in range(N):
            if nj + M > N:
                continue
            if ni == i and nj == j:
                continue
            if i * N + j > ni * N + j:
                continue
            flag = False
            for k in range(M):
                if visited[ni][nj + k]:
                    flag = True
            if flag:
                continue
            if not visited[ni][nj]:
                tmp = []
                for k in range(M):
                    visited[ni][nj + k] = True
                    tmp.append(arr[ni][nj + k])
                bee_box.append(tmp)
                select_map(idx + 1, ni, nj, visited)
                for k in range(M):
                    visited[ni][nj + k] = False
                bee_box.pop()



bee_box = []
mx = 0
for T in range(int(input())):
    mx = 0
    N, M, C = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_value = 0

    for i in range(N):
        for j in range(N):
            if j + M <= N:
                visited = [[False] * N for _ in range(N)]
                tmp = []
                for k in range(M):
                    visited[i][j + k] = True
                    tmp.append(arr[i][j + k])
                bee_box.append(tmp)
                select_map(1, i, j, visited)
                for k in range(M):
                    visited[i][j + k] = False
                bee_box.pop()

    print("#%d %d" % (T + 1, mx))