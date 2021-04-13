from itertools import combinations


def examine_press(d, w, k):

    for j in range(w):
        prev = arr[0][j]
        count = 1
        flag_possible = False
        for i in range(1, d):
            if prev == arr[i][j]:
                count += 1
                if count == k:
                    flag_possible = True
                    break
            else:
                count = 1
                prev = arr[i][j]
        if not flag_possible:
            return False
    return True


def inject_drug(num_list, d, w, sel_A):
    global arr
    val = 0
    for num in num_list:
        if num in sel_A:
            val = 0
        else:
            val = 1
        for j in range(w):
            arr[num][j] = val


for t in range(int(input())):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    number = [x for x in range(D)]
    flag = False
    ret = 0
    back = [a[:] for a in arr]

    for select_num in range(D + 1):
        comb = list(combinations(number, select_num))
        for com in comb:
            for i in range(len(com) + 1):
                sel_A = list(combinations(com, i))
                for sa in sel_A:
                    inject_drug(com, D, W, sa)
                    if examine_press(D, W, K):
                        ret = select_num
                        flag = True
                        break
                arr = [b[:] for b in back]
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    print("#%d %d" % (t + 1, ret))