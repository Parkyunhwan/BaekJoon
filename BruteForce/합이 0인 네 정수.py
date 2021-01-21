from collections import defaultdict
import sys

n = int(sys.stdin.readline())
a_list, b_list, c_list, d_list = [], [], [], []
ret = 0
for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

f_dict = defaultdict(int)
s_dict = defaultdict(int)
for a_val in a_list:
    for b_val in b_list:
        if not f_dict.get(a_val + b_val):
            f_dict[a_val + b_val] = 1
        else:
            f_dict[a_val + b_val] += 1

for c_val in c_list:
    for d_val in d_list:
        if not s_dict.get(c_val + d_val):
            s_dict[c_val + d_val] = 1
        else:
            s_dict[c_val + d_val] += 1

for key in f_dict.keys():
    if s_dict.get(-key):
        ret += (f_dict[key] * s_dict[-key])

print(ret)