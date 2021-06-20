from collections import defaultdict
for _ in range(int(input())):
    sentences = input()

    dic = defaultdict(int)
    for char in sentences:
        if char != ' ':
            dic[char] += 1

    dic = sorted(dic.items(), key=lambda x: -x[1])
    if len(dic) > 1 and dic[0][1] == dic[1][1]:
        print("?")
    else:
        print(dic[0][0])

