# https://marades.tistory.com/2
# velog
num = int(input())
word = []
for _ in range(num):
    word.append(input())

dic = {}
for w in word:
    i = 0
    for k in range(len(w)-1,-1,-1):
        if w[k] not in dic:
            dic[w[k]] = pow(10,i)
        else:
            dic[w[k]] += pow(10,i)
        i += 1

dic = sorted(dic.items(),  reverse=True, key=lambda x : x[1])

result = 0
k = 9
for d in dic:
    result += k*d[1]
    k -= 1
print(result)

# 모든 경우의 수를 구하는 방법 (시간 초과)
# import itertools
# num = int(input())
# word = []
# setword = set()
# for _ in range(num):
#     w = input()
#     for i in w:
#         setword.add(i)
#     word.append(w)
# setword=list(setword)
# per = [str(x) for x in range(9,9-len(setword),-1)]
# per = list(itertools.permutations(per,len(setword)))
#
#
# mx = -1
# for comp in per:
#     result = 0
#     for i in range(num):
#         rl = []
#         for w in word[i]:
#             rl.append(comp[setword.index(w)])
#         a = int( "".join(rl) )
#         result += a
#     mx = max(mx, result)
# print(mx)


