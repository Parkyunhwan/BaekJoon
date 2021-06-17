from collections import defaultdict
N = int(input())
arr = [input() for _ in range(N)]


count = 0
for word in arr:
    dic = defaultdict(int)
    flag = False
    prev = ''
    for i in range(len(word)):
        if prev != word[i]:
            if dic[word[i]] != 0:
                flag = True
                break
            dic[word[i]] += 1
            prev = word[i]

    if not flag:
        count += 1
print(count)