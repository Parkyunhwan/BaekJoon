'''
    2차원 배열에 대한 착각이 있었던 문제

    내가 2차원배열의 조합으로 풀고 싶었다면 x, y를 넘겨준다.
    이를 이용해 for문을 x, y로 시작하도록 설정한다.

    그럼 여기서 어떤 부분이 문제가 될까???
    ** 바로 y가 끝 부분을 만나서 다음 x로 넘어갈 때이다 **
    이 때 y는 0 부터 시작하지 않고 넘어온 y부터 시작하게 된다 ㅠㅠㅠ
'''


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

result = 1e9
flower = []


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def calc():
    sm = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                sm += arr[i][j]

    return sm

def dfs(index):
    global result
    if index == 3:
        result = min(result, calc())
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            flag = True
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if visited[nx][ny]:
                    flag = False
                    break
            if not flag:
                continue

            visited[i][j] = True
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                visited[nx][ny] = True

            dfs(index + 1)

            visited[i][j] = False
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                visited[nx][ny] = False

dfs(0)

print(result)