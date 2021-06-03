N = int(input())
li = list(input())
nums = [int(input()) for _ in range(N)]
output = []
for t in li:
    if t in "+-*/":
        a = output.pop()
        b = output.pop()
        if t == '+':
            output.append(b+a)
        elif t == '-':
            output.append(b-a)
        elif t == '*':
            output.append(b*a)
        elif t == '/':
            output.append(b/a)
    else:
        output.append(nums[ord(t)-ord('A')])
print("%.2f" % (output[0]))