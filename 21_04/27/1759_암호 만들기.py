from itertools import combinations
password = []
check = []
def dfs(idx, index, L, st):
    global password, check
    if idx == L:
        mo, ja = 0, 0
        for char in st:
            if char in "aeiou":
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            print(st)
        return

    for i in range(index, len(password)):
        if not check[i]:
            check[i] = True
            dfs(idx + 1, i + 1, L, st + password[i])
            check[i] = False



def solution():
    global password, check
    L, C = map(int, input().split())
    password = list(input().split())
    check = [False] * C
    password.sort()
    st = ""
    dfs(0, 0, L, st)
solution()