'''
    문제 로직은 맞은 문제

    %어디를 틀렸을까?%
        첫번째로 괄호의 짝을 체크할 때 스택을 사용하질 않아서 틀렸다.. -> ()()를 같은 숫자의 괄호짝으로 표시한 문제
        두번째는 41번째 줄에서 나올 수 있는 문자에 대한 `중복체크`를 해주지 않은 것이다. ex) (((abc))) 와 ((abc)) 중복이 가능하다.
'''
from itertools import combinations
string = list(input())

result = []

str_list = []
gh = []
num = 1
for val in string:
    if val == '(':
        gh.append(num) # 고친부분
        str_list.append(['(', num])
        num += 1
    elif val == ')':
        idx = gh.pop()
        str_list.append([')', idx])
    else:
        str_list.append([val])

tmp = [x for x in range(1, num)]
for i in range(1, num + 1):
    comb = combinations(tmp, i)
    for com in list(comb):
        curr = ''
        for i in range(len(str_list)):
            if len(str_list[i]) == 2:
                if not str_list[i][1] in com:
                    curr += str_list[i][0]
                    #print(str_list[i][0], end='')
            else:
                curr += str_list[i][0]
                #print(str_list[i][0], end='')
        #print()
        if curr not in result: # 고친부분
            result.append(curr)

result.sort()
for val in result:
    print(val)