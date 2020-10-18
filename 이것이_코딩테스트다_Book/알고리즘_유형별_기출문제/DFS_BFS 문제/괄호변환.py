# 1회차 -> x
# 재귀적인 것을 약간 이해하는 문제이면서 `구현`이 주가 되는 문제
# 균형잡힌 괄호 문자열

## -- 나동빈님 답 --
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)  # 균형잡힌 괄호의 index값을 반환
    u = p[:index + 1]  # 나랑 다른 점 -> 균형잡힌 괄호를 구한 후 문자열을 u와 v로분리
    v = p[index + 1:]  # 2번 지문과 똑같이 수행
    # 이제 3번 지문 -> 올바른 괄호 인지 확인
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        tmp = ""
        print(u[1:-1])
        for i in u[1:-1]:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        print(tmp)
        answer += tmp
    return answer







# 틀린 코드 -> 노력 ㅋ
def balance(u):
    if u == "":
        return ""
    left = 0
    right = 0
    pos = 0
    flag = False
    v = ""
    for i in range(len(u)):
        if u[i] == '(':
            left += 1
        else:
            right += 1
        if right > left:
            flag = True
        if left == right:
            pos = i
            break
        v = u[i + 1:]
    if flag:
        u = u[:i + 1] + balance(v)
    else:
        v = "(" + balance(v) + ")"
        u = u[1:-1]
        tmp = ""
        for c in u:
            if c == "(":
                tmp = tmp + ")"
            else:
                tmp = tmp + "("
        v = v + tmp
    return v


def solution(p):
    answer = ""
    if len(p) == 0:
        return p

    return balance(p)