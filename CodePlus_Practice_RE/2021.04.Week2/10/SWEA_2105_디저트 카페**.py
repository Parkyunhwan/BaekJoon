'''
    내가 풀려고 했던 방식은 내가 모든 경우의 수를 만들어서 제공하는 것이였다.

    현재 풀이에 사용한 방법은

    각 위치에서 '원래 가던 방향' 과 '꺽은 방향' 두가지 방법으로 갈 수 있고

    마지막 3번째 방향에서는 제 위치에서 꺽어줘야만 중복되는 탐색을 방지할 수 있다.
    이를 위해 처음 시작한 위치를 더한 값과 현재 위치를 더해서 같으면 꺽으면 원래 위치로 돌아갈 수 있다는 것을 이용한다.
    sx + sy == x + y

'''
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

dessert = [False] * 101


def dfs(x, y, l, d):
    global answer, dessert

    if d == 3 and x == sx and y == sy:
        answer = max(answer, l)
        return
    elif x < 0 or y < 0 or x >= N or y >= N:
        return
    elif dessert[arr[x][y]]:
        return

    dessert[arr[x][y]] = True

    if d == 0 or d == 1:
        dfs(x + dx[d], y + dy[d], l + 1, d)
        dfs(x + dx[d + 1], y + dy[d + 1], l + 1, d + 1)
    elif d == 2:
        if sx + sy != x + y:
            dfs(x + dx[d], y + dy[d], l + 1, d)
        else:
            dfs(x + dx[d + 1], y + dy[d + 1], l + 1, d + 1)
    else:
        dfs(x + dx[d], y + dy[d], l + 1, d)

    dessert[arr[x][y]] = False



answer = 0
sx, sy = 0, 0
for T in range(int(input())):
    answer = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            dfs(i, j, 0, 0)

    if answer == 0:
        answer = -1
    print("#%d %d" % (T + 1, answer))

