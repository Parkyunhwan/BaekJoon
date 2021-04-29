'''
    주석코드만 한번 보기.

'''

from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())

arr1, arr2 = [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr1.append([a, b])
    arr2.append([c, d])

dic1 = defaultdict(int)

for i in range(n):
    for j in range(n):
        sm = arr1[i][0] + arr1[j][1]
        dic1[sm] += 1

ret = 0
for i in range(n):
    for j in range(n):
        tmp = -(arr2[i][0] + arr2[j][1])
        if tmp in dic1:
            ret += dic1[tmp]

print(ret)

'''
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

        lt, rt = lp, rp
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


'''