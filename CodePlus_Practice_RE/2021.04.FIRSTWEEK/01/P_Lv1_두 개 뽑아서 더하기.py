from itertools import combinations


def solution(numbers):
    comb = list(combinations(numbers, 2))

    answer_set = set()
    for com in comb:
        print(com)
        answer_set.add(sum(com))

    answer = list(answer_set)
    answer.sort()
    return answer