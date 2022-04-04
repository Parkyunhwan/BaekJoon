N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]
answer = 0

def dfs(idx):
    global answer
    if idx == N * M:
        answer += 1
        return
    x, y = idx // M, idx % M

    # 현재 좌표를 채우지 않고 진행하는 경우
    dfs(idx + 1)

    if 0 < x < N and 0 < y < M and arr[x - 1][y] == 1 and arr[x][y - 1] == 1 and arr[x - 1][y - 1] == 1:
        pass
    else:
        # 현재 arr[x][y] 채우고 진행하는 경우 상, 좌, 상좌가 하나라도 0이 있을 때 채울 수 있음
        arr[x][y] = 1
        dfs(idx + 1)
        arr[x][y] = 0



dfs(0)
print(answer)
