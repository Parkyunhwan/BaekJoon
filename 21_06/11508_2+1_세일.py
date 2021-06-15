N = int(input())

price = [int(input()) for _ in range(N)]

price.sort(reverse=True)

stack = []
sum_value = 0
for i in range(N):
    if len(stack) == 2:
        sum_value += sum(stack)
        stack.clear()
    else:
        stack.append(price[i])

if stack:
    sum_value += sum(stack)

print(sum_value)
