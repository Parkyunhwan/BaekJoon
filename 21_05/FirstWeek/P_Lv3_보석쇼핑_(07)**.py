'''
    항상어려운 인덱스 처리
    https://programmers.co.kr/learn/courses/30/lessons/67258
'''

from collections import defaultdict
def solution(gems):
    answer = [1, len(gems)]
    gemset = set(gems)
    bag = defaultdict(int)

    s, e = 0, 0
    while e < len(gems):
        if len(bag) < len(gemset):
            bag[gems[e]] += 1
            e += 1
        else:
            if bag[gems[s]] == 1:
                del bag[gems[s]]
            else:
                bag[gems[s]] -= 1
            if answer[1] - answer[0] > e - s - 1:
                answer = [s + 1, e]
            s += 1
    return answer

'''

'''
from collections import defaultdict


def solution(gems):
    answer = [0, len(gems) - 1]
    count = defaultdict(int)

    gemlength = len(set(gems))
    gemset = set()
    i = 0
    j = 0

    count[gems[0]] += 1
    gemset.add(gems[0])
    while j < len(gems) and i < len(gems):
        if len(gemset) == gemlength:

            left, right = answer
            if right - left > j - i:
                answer = [i, j]
            count[gems[i]] -= 1
            if count[gems[i]] == 0:
                gemset.discard(gems[i])
            i += 1
        else:
            j += 1
            if j == len(gems):
                break
            if count[gems[j]] == 0:
                gemset.add(gems[j])
            count[gems[j]] += 1
    return [answer[0] + 1, answer[1] + 1]



gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))