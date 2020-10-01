import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
left_arr, right_arr = [], []
for i in range(n):
    for j in range(n):
        left_arr.append(arr[i][0] + arr[j][1])
        right_arr.append(arr[i][2] + arr[j][3])


left_arr.sort()
right_arr.sort()

ans = 0

len_ls, len_rs = len(left_arr), len(right_arr)
lp, rp = 0, len_rs - 1
while lp < len_ls and rp >= 0:
    tmp = left_arr[lp] + right_arr[rp]

    # 더해서 답과 같다면 이제 중복된 값을 계산해줘야 한다.
    if tmp == 0:
        lsame, rsame = 1, 1

        lt, rt = lp, rp  # 투 포인트 사용 시 주의해야할 점
                         # 원하는 합의 위치를 기억해둬야 한다.
        lp += 1
        while lp < len_ls and left_arr[lp] + right_arr[rt] == 0:
            # (소팅된 리스트에서)같은 숫자 갯수 세기
            lsame += 1
            lp += 1

        rp -= 1
        while rp >= 0 and left_arr[lt] + right_arr[rp] == 0:
            rsame += 1
            rp -= 1

        ans += (lsame * rsame) # 중복 숫자 끼리 곱해줘야 그만큼의 갯수가 나온다.
    # if문을 나오면 해당 합의 중복이 제외된다.

    elif tmp < 0:
        lp += 1
    else:
        rp -= 1
print(ans)

#  딕셔너리를 이용한 투 포인트 방법..
import sys
n = int(sys.stdin.readline())
alist, blist, clist, dlist = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    alist.append(a); blist.append(b); clist.append(c); dlist.append(d)
ab, cd = {}, {}
for a in alist:
    for b in blist:
        if not ab.get(a+b):
            ab[a+b] = 1
        else:
            ab[a+b] += 1

for c in clist:
    for d in dlist:
        if not cd.get(c+d):
            cd[c+d] = 1
        else:
            cd[c+d] += 1
ans = 0
for _, key in enumerate(ab):
    if cd.get(-key):
        ans += (ab[key] * cd[-key])
print(ans)

