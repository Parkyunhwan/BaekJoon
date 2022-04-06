import sys
T = input()
N = int(input())

info = []
infoVisited = [0] * N
currPay = 0

minSum = sys.maxsize


def myInput():
    for i in range(N):
        inp = input().split(" ")
        info.append([int(inp[0]), inp[1]])


def solve(idx, pay):
    global minSum

    if pay > minSum:
        return

    if idx == len(T):
        minSum = pay
        return

    ch = T[idx]
    for i in range(N):
        curr = info[i]
        if ch in curr[1]:
            curr[1] = curr[1].replace(ch, '*', 1)
            if infoVisited[i] == 0:
                pay += curr[0]
            infoVisited[i] += 1
            solve(idx + 1, pay)
            infoVisited[i] -= 1
            if infoVisited[i] == 0:
                pay -= curr[0]
            curr[1] = curr[1].replace('*', ch, 1)

myInput()
solve(0, 0)
print(-1 if minSum == sys.maxsize else minSum)