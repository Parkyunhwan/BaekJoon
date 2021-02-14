n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
mx = 0

for k in range(1 << (n * m)): # 1 0000 0000 0000 0000 (4 * 4) [모든 경우의 수를 비트로 표현]
    sm = 0
    caro = 0
    sero = 0
    for i in range(n):
        for j in range(m):
            idx = m * i + j # [1차원 -> 2차원]
            if (1 << idx) & k: # 현재 인덱스가 가로인지 세로인지 판단
                caro = caro * 10 + arr[i][j]
            else:
                sm += caro # 세로라면 현재까지 값을 모두 더해둠
                caro = 0
        sm += caro # 끝날 때까지 가로일 수 있으므로 더해준다.
        caro = 0

    for j in range(m):
        for i in range(n):
            idx = m * i + j
            if (1 << idx) & k == 0:
                sero = sero * 10 + arr[i][j]
            else:
                sm += sero
                sero = 0
        sm += sero
        sero = 0
    mx = max(mx, sm)
print(mx)
