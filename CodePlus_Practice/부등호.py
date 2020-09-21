import itertools

num=input()
sign = input().split()
val=[str(x) for x in range(10)]
per = list(itertools.permutations(val, int(num)+1))
flag = 0
min_v = '9999999999'
max_v = '-1'
for comp in per:
    flag=0
    for i in range(int(num)):
        if sign[i]== '<' and comp[i] < comp[i + 1]:
            flag += 1
        elif sign[i]== '>' and comp[i] > comp[i + 1]:
            flag += 1
        else:
            break
    if flag == int(num):
        min_v = min(min_v, str(''.join(comp)))
        break


for k in range(len(per)-1,0,-1):
    flag=0
    for i in range(int(num)):

        if(sign[i]=='<' and per[k][i] < per[k][i+1]):
            flag += 1
        elif(sign[i]=='>' and per[k][i] > per[k][i+1]):
            flag += 1
        else:
            break
    if flag == int(num):
        max_v = max(max_v, str(''.join(per[k])))
        break
print(max_v)
print(min_v)




