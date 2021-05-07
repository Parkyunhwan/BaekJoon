'''
    index 해결이 조금 힘들엇던 문제

    temp 리스트를 둬야만 모든 조건을 탐색할 수 있다.
    index 문제는 항상 꼼꼼히.

'''
import re
from itertools import permutations


def calculate(a, b, oper):
    if oper == '*':
        return a * b
    elif oper == '+':
        return a + b
    else:
        return a - b


def solution(expression):
    answer = 0

    nums = re.split("[*+-]", expression)
    oper = re.split("\d+", expression)
    nums = list(map(int, nums))

    oper = oper[1:-1]
    operation = list(set(oper))
    perm = permutations(operation, len(operation))

    for per in list(perm):
        toper = oper[:]
        tnums = nums[:]

        for char in per:
            i = 0
            while i < len(toper):
                curr = toper[i]
                if curr == char:
                    num1 = tnums[i]
                    num2 = tnums[i + 1]
                    sum_value = calculate(num1, num2, char)
                    del tnums[i + 1]
                    del toper[i]
                    tnums[i] = sum_value
                else:
                    i += 1
        answer = max(answer, abs(tnums[0]))
    return answer