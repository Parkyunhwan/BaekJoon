'''
    N사 인턴
    비슷한문제
'''
N = int(input())

arr = list(map(int, input().split()))

stack = []

stack.append([0, arr[0]])

result = [-1] * N
for i in range(1, len(arr)):
    while stack:
        if stack[-1][1] < arr[i]:
            idx, val = stack.pop()
            result[idx] = arr[i]
        else:
            break
    stack.append([i, arr[i]])

for val in result:
    print(val, end=' ')

