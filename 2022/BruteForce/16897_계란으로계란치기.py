N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

start_egg = eggs[0]

result = 0
def solve(currEgg):
    global result

    if currEgg >= N:
        count = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                count += 1
        result = max(result, count)
        return

    # 손에든 계란이 깨졌을 때 치지않고 다음 계란으로 진행
    if eggs[currEgg][0] <= 0:
        solve(currEgg + 1)
    else: # 손에든 계란이 깨지지 않았을 때 다른 계란을 부딪혀봄
        flag = False
        for nextEgg in range(N):
            if nextEgg == currEgg:
                continue
            eggInfo = eggs[nextEgg]
            if eggInfo[0] <= 0 and eggs[currEgg][0] > 0: # 조건을 여기에 몰아서 사용해도 됨
                continue
            eggInfo[0] -= eggs[currEgg][1]
            eggs[currEgg][0] -= eggInfo[1]
            flag = True
            solve(currEgg + 1)
            eggInfo[0] += eggs[currEgg][1]
            eggs[currEgg][0] += eggInfo[1]

        # 단하나라도 부딪힐 계란이 없다면 계산 (종료)
        if flag == False:
            solve(N)

solve(0)
print(result)