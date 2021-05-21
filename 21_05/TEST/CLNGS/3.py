from itertools import combinations
N = int(input())
arr = [list(map(int, input().strip().split(' '))) for _ in range(N)]
mn = 1e9

allmember = [x for x in range(N)]
def dfs(index, start, team):
    global mn
    if index == N // 2:
        score1, score2 = 0, 0

        # 첫번째 팀의 시너지 점수 score1
        comb = combinations(team, 2)
        for com in list(comb):
            first, second = com
            score1 += arr[first][second]

        # 두번째 팀의 시너지 점수 score1
        team2 = set(allmember) - set(team)
        comb = combinations(team2, 2)
        for com in list(comb):
            first, second = com
            score2 += arr[first][second]

        # 시너지의 차이의 최솟값을 구함
        if mn > abs(score1 - score2):
            mn = abs(score1 - score2)
        return

    for i in range(start, N):
        if i not in team:
            team.append(i)
            dfs(index + 1, i + 1, team)
            team.pop()

dfs(0, 0, [])
print(mn)