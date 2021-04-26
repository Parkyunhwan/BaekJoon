def solution(n):
    answer = ''
    '''
    https://itholic.github.io/kata-124-world/
    사실상 4가 0의 역할을 하지만 3의 값과 같다. 3을 3진법으로 표현하면 10이다.

     하지만 124나라는 0을 표현할 수 없으므로 3을 "4"로 표현하게 되고
     6 -> 3진법:20 -> 124진법: "14" 로 표현하게 된다.
     7 -> 3진법:21 -> 124진법: "21"

     즉, 3으로 나눠지는 값에 대해 -1한 값이되어야만 한다.
    '''
    ott = ['4', '1', '2']  # 나머지가 0 일 때 4를 반환한다. (0의 개념이 없으므로)
    while n != 0:
        n, mod = divmod(n, 3)
        answer = ott[mod] + answer
        if mod == 0:
            n -= 1

    return answer