# coding=utf-8
import sys
n = int(input())
m = int(input())
curr = 100
if m > 0:
    malf = input().split()
else:
    malf = []

channels = []
diff = abs(n-100)
min_diff = sys.maxsize
for i in range(1000000+1):
    flag=False
    str_i = str(i)
    for j in str_i:
        if j in malf:
            flag=True
            break
    if flag:
        pass
    else:
        length = len(str(i))
        val = abs(i-n)
        min_diff = min(min_diff, length+val)

diff = min(diff, min_diff)
print(diff)

