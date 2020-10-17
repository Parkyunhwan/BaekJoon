# Facebook 인터뷰
mystr = list(input())
alpha = []
number = []
for s in mystr:
    if ord('A') <= ord(s) <= ord('Z'):
        alpha.append(s)
    else:
        number.append(int(s))
alpha.sort()
sm = sum(number)

result = ''.join(alpha) + str(sm)
print(result)
