'''
    '사다리 타기'의 특성을 생각해봐야 한다.

    사다리 타기를 배열로 표현 하면 - |   | - 형태도 배열에서는 True | True 형태로 나오게 된다.

    나는 처음에 True | False | True 여야만 가능한 줄 착각해서 코드를 어렵게 짜고도 답을 구해내지 못했다.

    문제는 간단히 dfs를 통해 가능한 사다리 배치를 한다.
    사다리 배치가 끝난 후 그 사다리 배치에 대해 가능한지 검사한다.

    가능한 사다리 배치가 있다면 출력하면 된다.

    이 문제에서 기억해야할 점은 조합처럼 다음 사다리의 선택 지점을 이전 지점 뒤를 선택해야한다.
    이렇게 하지 않고 순열처럼 처음부터 선택하며 중복해서 검사하는 숫자가 훨씬 증가하게 된다.
'''
N, M, H = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(H + 1)]

def check_possible():
    for j in range(1, N + 1):
        curr_j = j
        for i in range(1, H + 1):
            if arr[i][curr_j]:
                if arr[i][curr_j - 1] == arr[i][curr_j]:
                    curr_j -= 1
                elif curr_j != N and arr[i][curr_j + 1] == arr[i][curr_j]:
                    curr_j += 1
        if j != curr_j:
            return False
    return True



def set_sadari(x, y, num):
    global flag
    if num == 0:
        if check_possible():
            flag = True
        return
    for i in range(x, H + 1):
        for j in range(1, N):
            if not arr[i][j] and not arr[i][j + 1]:
                arr[i][j] = num
                arr[i][j + 1] = num
                set_sadari(i, j, num - 1)
                arr[i][j] = 0
                arr[i][j + 1] = 0

flag = False
for tt in range(M):
    a, b = map(int, input().split())
    arr[a][b] = tt + 4
    arr[a][b + 1] = tt + 4

for num in range(0, 4):
    set_sadari(1, 1, num)
    if flag:
        print(num)
        exit(0)

print(-1)
