def DFS(index, val):
    global mx, mn
    if index == n-1:
        mx = max(mx, val)
        mn = min(mn, val)
        return
    for i in range(len(oper)):
        if check[i]:
            continue
        check[i] = True
        if oper[i] == 0:
            DFS(index + 1, val + num[index+1])
        elif oper[i] == 1:
            DFS(index + 1, val - num[index+1])
        elif oper[i] == 2:
            DFS(index + 1, val * num[index+1])
        else:
            DFS(index + 1, val//num[index+1] if val > 0 else -((-val)//num[index+1]))
        check[i] = False

n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
oper = []
for i in range(len(operator)):
    for j in range(operator[i]):
        oper.append(i)

check = [False]*len(oper)

mx = int(-1e9)
mn = int(1e9)
sm = num[0]
DFS(0, sm)
print(mx)
print(mn)

# ✓ 음수를 양수로 나누는 경우, 파이썬과 C++의 방식이 다르다.
# ✓ 문제 보기에 주어진 내용처럼, 음수를 양수로 바꾼 후 몫을 먼저 구하고, 그 몫을 음수로 다시 바꿔야 한다.
