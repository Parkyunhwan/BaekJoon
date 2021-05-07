'''
    카카오 인턴 문제

    시간 초과를 생각하면 '이게 될까' 의문이 들때도 일단 해봐야 한다.

    범위가 작았기 때문에

    ''.join() 과 sort() 를 활용해서 어떻게든 중복체크를 했다면 고민을 덜 수 있는 문제였다.

    -> '효율성 체크'가 없다면 일단 구현에 집중하자.


'''

visited = set()
mx = 0


def dfs(idx, banlist, duplist):
    global mx
    if idx == len(banlist):
        dup = sorted(duplist)
        dup = ''.join(dup)

        if dup not in visited:
            visited.add(dup)
            mx += 1
        return

    bans = banlist[idx]
    for i in range(len(bans)):
        if bans[i] not in duplist:
            duplist.append(bans[i])
            dfs(idx + 1, banlist, duplist)
            duplist.pop()


def solution(user_id, banned_id):
    answer = 0

    banlist = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if len(user) != len(ban):
                continue
            flag = True
            for i in range(len(user)):
                if ban[i] == '*' or ban[i] == user[i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                tmp.append(user)
        banlist.append(tmp)
    print(banlist)
    dfs(0, banlist, [])
    return mx