'''
    210512 - 구현 dfs
    dfs이용한 조합시에는

    현재 dfs깊이와 현재 curr_idx 번호가 필요하다 (idx, depth라고 하는게 좋을 것 같다)
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
selected = [0] * (N + 1)
min_diff = 1e9

def dfs(curr, index):
    global min_diff
    if index == N // 2:
        start_team = 0
        link_team = 0
        for i in range(N):
            for j in range(N):
                if selected[i] == 1 and selected[j] == 1:
                    start_team += arr[i][j]
                elif selected[i] == 0 and selected[j] == 0:
                    link_team += arr[i][j]

        min_diff = min(min_diff, abs(start_team - link_team))

    for i in range(curr + 1, N):
        selected[i] = 1
        dfs(i, index + 1)
        selected[i] = 0


dfs(0, 0)
print(min_diff)