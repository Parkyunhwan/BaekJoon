from itertools import combinations

def solution(nums):
    answer = 0
    sum_list = []
    comb = list(combinations(nums, 3))

    for com in comb:
        sm = 0
        for val in com:
            sm += val
        sum_list.append(sm)

    for val in sum_list:
        flag = True
        for j in range(2, val):
            if val % j == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer