'''
    https://programmers.co.kr/learn/courses/30/lessons/42862
'''


def solution(n, lost, reserve):
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))

    for val in _reserve:
        minus = val - 1
        plus = val + 1
        if minus in _lost:
            _lost.remove(minus)
        elif plus in _lost:
            _lost.remove(plus)

    return n - len(_lost)