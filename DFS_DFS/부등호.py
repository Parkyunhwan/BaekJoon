import sys

n = int(input())
oper = input().split()
check = [False] * 10
v = []
mn = sys.maxsize
mn_str = ""
mx = -1
mx_str = ""


def possible(i):
    if oper[i - 1] == '>' and v[i - 1] < v[i]:
        return False
    elif oper[i - 1] == '<' and v[i - 1] > v[i]:
        return False
    return True


def dfs(idx):
    global mn, mx, mn_str, mx_str
    if idx == n + 1:
        v_str = ''.join(map(str, v))
        val = int(v_str)
        if mn > val:
            mn = val
            mn_str = v_str
        elif mx < val:
            mx = val
            mx_str = v_str
        return
    else:
        for i in range(10):
            if check[i] is True:
                continue
            check[i] = True
            v.append(i)
            if idx == 0 or possible(idx):
                dfs(idx + 1)
            check[i] = False
            v.pop()


dfs(0)
print(mx_str)
print(mn_str)
