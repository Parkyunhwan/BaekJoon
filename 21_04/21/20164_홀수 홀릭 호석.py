from itertools import combinations
N = input()

min_value = 1e9
max_value = 0


def dfs(n, odd_num):
    global min_value, max_value
    nlist = list(n)
    for val in nlist:
        v = int(val)
        if v % 2 == 1:
            odd_num += 1

    length = len(nlist)
    if length == 1:
        # odd_num을 이용해 최대 최소 갱신
        min_value = min(odd_num, min_value)
        max_value = max(odd_num, max_value)
        return
    elif length == 2:
        number = int(nlist[0]) + int(nlist[1])
        dfs(str(number), odd_num)
    else:
        tmp_num = [i for i in range(1, length)]
        comb = combinations(tmp_num, 2)
        for com in list(comb):
            part1 = nlist[:com[0]]
            part2 = nlist[com[0]:com[1]]
            part3 = nlist[com[1]:]
            sum_value = int(''.join(part1)) + int(''.join(part2)) + int(''.join(part3))
            dfs(str(sum_value), odd_num)

dfs(N, 0)
print("%d %d" % (min_value, max_value))