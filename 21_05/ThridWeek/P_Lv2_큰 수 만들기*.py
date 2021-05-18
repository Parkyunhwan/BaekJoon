'''
    스택을 이용하자.

    현재 스택의 top보다 작은 값은 무조건 삽입하고
    top보다 큰 값은 더 큰 값이 상단에 올때까지 pop()한다.

    이 작업을 k == 0이 될 때까지 또는 전체 문자열을 검사할 때 까지 진행한다.

    이 작업을 거치면 스택에는 "앞자리 숫자가 가장 큰 순서"를 가지게 된다.
    -> 앞자리를 최고 큰 수로 만들기 전략!!

    ## 주의할 점 ##
    k의 갯수보다 적게 삭제하는 경우가 있을 수 있다. ex) 17442, k = 3 -> 처리를 거치면 7442가 나옴

    남은 k가 2 이므로 스택의 뒤에서 부터 2를 pop()해준다. answer -> 74
'''
def solution(number, k):
    answer = ''
    stack = []

    for idx, num in enumerate(number):
        while stack and k > 0:
            if stack[-1] < num:
                stack.pop()
                k -= 1
            else:
                break

        stack.append(num)

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)