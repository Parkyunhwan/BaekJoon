'''
    예외 처리와 '스택 개념' + 괄호 처리 개념이 필요했다.

    스택만 사용하지 말고 각각의 괄호에 번호를 부여해야 더쉽게 풀 수 있다.
    괄호가 열린괄호 후 바로 닫혔다면 (값)을 가질 수 있고
    열린 괄호 후에 바로 닫히지 않았다면 따로 더해지는 값으로 처리하지 않는다.

    그런데 이 방법은 스택을 이용한다는 느낌은 조금 적은 방법이였다.

    이것말고 '스택을 좀 더 활용한 방법'으로 풀이해보자.
'''
# 스택을 더 활용한 방법
gwalho = list(input())

stack = []

sum_value = 1
result = 0
for i, val in enumerate(gwalho):
    if val == '(':
        stack.append(val)
    elif val == '[':
        stack.append(val)
    else:
        if not stack:

            print(0)
            exit(0)

        if val == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                curr = 0
                while stack:
                    top = stack[-1]

                    if top == "[":

                        print(0)
                        exit(0)
                    elif top == "(":
                        stack.pop()
                        curr *= 2
                        stack.append(curr)
                        break
                    else: # "2", "3.."
                        curr += stack.pop() # number value
                result += curr
        elif val == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                curr = 0
                while stack:
                    top = stack[-1]

                    if top == "(":
                        print(0)
                        exit(0)
                    elif top == "[": # stack 안에서 짝을 만나면 while문 빠져나옴!
                        stack.pop()
                        curr *= 3
                        k = 1
                        stack.append(curr)
                        break
                    else:  # "2", "3.."
                        curr += stack.pop()  # number value
                        k = 2
                result += curr

result = 0
while stack:
    if stack[-1] == '(' or stack[-1] == ')' or stack[-1] == '[' or stack[-1] == ']':
        print(0)
        exit(0)
    else:
        result += stack.pop()

print(result)


# 스택이 덜 사용된 방법
'''
gwalho = list(input())

stack = []

sum_value = 1
result = 0
for i, val in enumerate(gwalho):
    if val == '(':
        sum_value = sum_value * 2
        stack.append(val)
    elif val == '[':
        sum_value = sum_value * 3
        stack.append(val)
    else:
        if val == ')' and stack and stack[-1] == '(':
            if gwalho[i - 1] == '(':
                result += sum_value
            stack.pop()
            sum_value //= 2
        elif val == ']' and stack and stack[-1] == '[':
            if gwalho[i - 1] == '[':
                result += sum_value
            stack.pop()
            sum_value //= 3
        else:
            print(0)
            exit(0)

if stack:
    print(0)
    exit(0)
print(result)
'''