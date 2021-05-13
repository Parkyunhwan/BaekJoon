'''
    스택 관련 문제

    스택은 '가장 가까운', '같은' 등 여러 조건에서 사용할 수 있다.

    또한, 시간제한이 있는 문제에서 많이 사용되는 것같다.

    문제가 안풀리다면 스택을 한번 고민해보도록 하자.

'''

def solution(s):
    answer = 0

    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        answer = 0
    else:
        answer = 1
    return answer