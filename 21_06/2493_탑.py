'''
    1 <= N <= 500000 이므로 N^2 가 불가능하다.

    stack을 이용해서 풀이
'''
n = int(input())

arr = list(map(int, input().split()))
result = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    if not stack:
        stack.append((arr[i], i))
    else:
        while stack and arr[i] > stack[-1][0]:
            result[stack[-1][1]] = (i + 1)
            stack.pop()
        else:
            stack.append((arr[i], i))

for r in result:
    print(r, end=' ')