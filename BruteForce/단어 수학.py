n = int(input())
ch = [0] * 26
arr = [input() for _ in range(n)]
alpha = []
v = []
check = [False] * 10
result = 0
for w in arr:
    for i in range(0, len(w)):
        if not ch[ord(w[i]) - ord('A')]:
            ch[ord(w[i]) - ord('A')] = True
            alpha.append(w[i])

def calculate():
    global result
    tmpAlpha = [0] * 26
    for i in range(len(alpha)):
        c = alpha[i]
        val = v[i]
        tmpAlpha[ord(c) - ord('A')] = val
    allword = 0
    for w in arr:
        tmp = 0
        for i in range(len(w)):
            tmp *= 10
            tmp += tmpAlpha[ord(w[i]) - ord('A')]
        allword += tmp
    result = max(result, allword)


def dfs(index):
    if index == 10:
        calculate()
    else:
        for i in range(10 - len(alpha), 10):
            if check[i]:
                continue
            v.append(i)
            check[i] = True
            dfs(index + 1)
            check[i] = False
            v.pop()


dfs(10 - len(alpha))
print(result)
