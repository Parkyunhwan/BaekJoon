from itertools import combinations

 

n, s = map(int, input().split())

arr = list(map(int, input().split()))

left, right = arr[:n//2], arr[n//2:]

 

l_sum, r_sum = [], []

for i in range(n//2 + 1):

    cm = list(combinations(left, i))

    for c in cm:

        l_sum.append(sum(c))

for i in range(n - n//2 + 1):

    cm = list(combinations(right, i))

    for c in cm:

        r_sum.append(sum(c))

l_sum.sort(); r_sum.sort()

 

ans = 0

len_ls, len_rs = len(l_sum), len(r_sum)

lp, rp = 0, len_rs-1

while lp < len_ls and rp >= 0:

    tmp = l_sum[lp] + r_sum[rp]

 

    if tmp == s:

        lsame, rsame = 1, 1

 

        lt, rt = lp, rp

        lp += 1

        while lp < len_ls and l_sum[lp] == l_sum[lt]:

            lsame += 1

            lp += 1

        rp -= 1

        while rp >= 0 and r_sum[rp] == r_sum[rt]:

            rsame += 1

            rp -= 1

        

        ans += (lsame * rsame)

    elif tmp < s:

        lp += 1

    else: # tmp > s

        rp -= 1

 

print(ans-1 if s == 0 else ans)

