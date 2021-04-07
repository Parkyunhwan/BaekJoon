def solution(n):
    answer = []

    idx = 1
    while n >= pow(3, idx):
        idx += 1
    idx -= 1

    while idx >= 0:
        val = pow(3, idx)
        ret = n // val
        n = n - (val * ret)
        answer.append(ret)
        idx -= 1
    answer.reverse()

    length = len(answer)
    p = 0
    result = 0
    for i in range(length - 1, -1, -1):
        val = answer[i]
        zecob = pow(3, p)
        result += (zecob * val)
        p += 1

    return result

'''
def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3) # 나머지는 해당 3의 자릿수의 값이된다.
        n = n//3    # 몫은 다음에 계산할 값을 뜻한다.
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer
'''