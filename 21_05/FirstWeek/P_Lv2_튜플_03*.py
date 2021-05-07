'''
    내 코드
'''

def solution(s):
    s = s[1:-1]
    answer = []
    stack = []
    num = ""
    for val in s:
        if val in '{':
            stack = []
        elif val == ',':
            if len(num) != 0:
                stack.append(int(num))
                num = ""
        elif val.isdigit():
            num = num + val
        elif val in '}':
            if len(num) != 0:
                stack.append(int(num))
            answer.append(stack)
            num = ""

    set1 = set()
    size = len(answer)
    result = [0] * size

    for i in range(1, size + 1):
        for val in answer:
            if len(val) == i:
                diff = set(val) - set1
                set1.update(diff)
                result[i - 1] = list(diff)[0]

    return result

'''
    다른사람코드
    "},{"를 통한 split 사용.
    len(x)길이로 정렬하기.
'''
def solution(s):
    answer = []
    s = s[2:-2]
    s = sorted(s.split("},{"), key = lambda x: len(x))

    for i in s:
        i_ = i.split(',')
        for j in i_:
            if int(j) not in answer:
                answer.append(int(j))
    return answer