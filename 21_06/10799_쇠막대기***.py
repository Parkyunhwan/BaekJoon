'''
https://blog.joonas.io/86

레이저를 쏜 당시의 막대의 갯수만큼을 더한다.

이후에도 똑같이 레이저를 쏜 당시의 막대 갯수 만큼 더하면 된다.

하지만, 막대의 끝 부분을 만난 경우(층이 바뀌는 경우) 반드시 1을 더해줘야만 한다.
'''
arr = input()
result = 0
stack = []

for i, val in enumerate(arr):
    if val == '(':
        stack.append(val)
    else:
        stack.pop()
        if arr[i - 1] == ')': # arr[i] == ')'
            result += 1 # 현재 라인 추가 (레이저 아닐 때)
        else:
            result += len(stack)

print(result)