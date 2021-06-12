arr = input()

stack = []
result = 0
for i in range(len(arr)):
    if arr[i] == '(' or arr[i] == '[':
        stack.append(arr[i])
    else:
        if not stack:
            print(0)
            exit(0)

        if arr[i] == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                curr = 0
                while stack:
                    value = stack.pop()
                    if value == '[':
                        print(0)
                        exit(0)
                    elif value == '(':
                        curr *= 2
                        stack.append(curr)
                        break
                    else:
                        curr += value

        elif arr[i] == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                curr = 0
                while stack:
                    value = stack.pop()
                    if value == '(':
                        print(0)
                        exit(0)
                    elif value == '[':
                        curr *= 3
                        stack.append(curr)
                        break
                    else:
                        curr += value


result = 0
while stack:
    if stack[-1] == '(' or stack[-1] == ')' or stack[-1] == '[' or stack[-1] == ']':
        print(0)
        exit(0)
    else:
        result += stack.pop()

print(result)