from collections import defaultdict, deque
string = input()
dic = defaultdict(int)
for s in string:
    dic[s] += 1

front = deque()
back = deque()
keys = sorted(list(dic.keys()))
remain = []
count = 0
for key in keys:
    num = dic[key]
    if num > 0:
        for _ in range(num // 2):
            front.append(key)
            back.appendleft(key)

        if num % 2 == 1:
            count += 1
            remain.append(key)
if count > 1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(list(front)) + ''.join(remain) + ''.join(list(back)))

