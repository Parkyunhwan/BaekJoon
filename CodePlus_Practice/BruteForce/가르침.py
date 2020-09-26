#https://dirmathfl.tistory.com/176
from sys import stdin, exit

mx = 0
# n, k = map(int, input().split())
n, k = map(int, stdin.readline().split())
if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)
k -= 5
arr = [stdin.readline().rstrip()[4:-4] for _ in range(n)]
ch = [0] * 26


def solve(start, index):
    global mx
    if index == k:
        result = 0
        for ar in arr:
            for a in ar:
                if ch[ord(a) - ord('a')] == 0:
                    break
            else:
                result += 1
        mx = max(mx, result)
        return

    for i in range(start, 26):
        if ch[i] == 0:
            ch[i] = 1
            solve(i, index + 1)
            ch[i] = 0


for c in ('a', 'c', 'i', 'n', 't'):
    ch[ord(c) - ord('a')] = 1

solve(0, 0)
print(mx)
# 시간 초과..
# from sys import stdin, exit
# mx = 0
# # n, k = map(int, input().split())
# n, k = map(int, stdin.readline().split())
# if k < 5:
#     print(0)
#     exit(0)
# elif k == 26:
#     print(k)
#     exit(0)
# k -= 5
# arr = [stdin.readline().rstrip()[4:-4] for _ in range(n)]
# nli = []
# ch = [0] * 26
# set_n = 0
#
#
# def solve(start, index):
#     global mx
#     if index == k:
#         result = 0
#         for i in nli:
#             flag = True
#             for j in i:
#                 if ch[j] == 0:
#                     flag = False
#                     break
#             if flag:
#                 result += 1
#         mx = max(mx, result)
#     else:
#         for i in range(start, len(val)):
#             tmp = val[i]
#             if ch[tmp] == 0:
#                 ch[tmp] = 1
#                 solve(tmp, index + 1)
#                 ch[tmp] = 0
#
#
# basic = ['a', 'c', 'i', 'n', 't']
# val = set()
# for b in basic:
#     diff = ord(b)-ord('a')
#     val.add(diff)
#     ch[diff] = 1
#
# for a in arr:
#     temp = []
#     for v in a:
#         diff = ord(v) - ord('a')
#         temp.append(diff)
#         val.add(diff)
#     nli.append(temp)
# val = list(val)
# solve(0, 0)
# print(mx)
