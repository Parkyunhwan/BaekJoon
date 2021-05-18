def getYapsu(number):
    ret = 1
    for i in range(2, number + 1):
        if number % i == 0:
            ret += 1
    return ret

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        ret = getYapsu(num)
        if ret % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer