from collections import Counter

def solution(topping):
    if len(topping) == 1:
        return 0

    answer = 0
    dic = Counter(topping)
    topping_set = set()

    for top in topping:
        dic[top] -= 1
        topping_set.add(top)
        if dic[top] == 0:
            dic.pop(top)
        if len(dic) == len(topping_set):
            answer += 1

    return answer