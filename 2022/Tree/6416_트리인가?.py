from collections import defaultdict
li = []
count = 1

def possibleTree(li):
    if not li:
        print(f'Case {count} is a tree')
        return
    dic = defaultdict(int)
    flag1 = True
    s = set()
    for a, b in li:
        dic[b] += 1
        s.add(a)
        s.add(b)
    root = -1
    for u in s:
        if dic[u] == 0:
            if root == -1:
                root = u
            else:
                flag1 = False
                break
        else:
            if dic[u] > 1:
                flag1 = False
                break

    if root == -1:
        flag1 = False
    if flag1:
        print(f'Case {count} is a tree.')
    else:
        print(f'Case {count} is not a tree.')
    return


while True:

    val = input()
    if val == '-1 -1':
        break

    inp = val.split('  ')
    flag = True

    for com in inp:

        sp = list(map(int, com.split()))

        if (sp[0], sp[1]) == (0, 0):
            possibleTree(li)
            count += 1
            flag = False
            break
        li.append([sp[0], sp[1]])
    if flag:
        continue
    li = []
    input()