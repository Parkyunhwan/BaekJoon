# https://suri78.tistory.com/168
# 2^20 은 10^6 -- 2^40 은 10^12
# 1억은 10^8 (시간복잡도 계산 시 사용)
# 40개의 모든 조합을 만들기 위해선 O(2^40) 만큼이 필요하다.
# 따라서 조합을 반절 씩 나눠 모든 조합을 구하고 그 합을 투 포인터로 구해서 답을 구한다.
from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = arr[:n//2], arr[n//2:]

l_sum, r_sum = [], []
count = 0
for i in range(n//2+1):
    cm = combinations(left, i)
    for c in cm:
        l_sum.append(sum(c))
for i in range(n - n//2 + 1):
    cm = combinations(right, i)
    for c in cm:
        r_sum.append(sum(c))
l_sum.sort(); r_sum.sort()

ans = 0
len_ls, len_rs = len(l_sum), len(r_sum)
lp, rp = 0, len_rs-1

while lp < len_ls and rp >= 0:
    tmp = l_sum[lp] + r_sum[rp]

    # 더해서 답과 같다면 이제 중복된 값을 계산해줘야 한다.
    if tmp == s:
        lsame, rsame = 1, 1

        lt, rt = lp, rp
        lp += 1
        while lp < len_ls and l_sum[lp] == l_sum[lt]:
            # (소팅된 리스트에서)같은 숫자 갯수 세기
            lsame += 1
            lp += 1

        rp -= 1
        while rp >= 0 and r_sum[rp] == r_sum[rt]:
            rsame += 1
            rp -= 1

        ans += (lsame * rsame) # 중복 숫자 끼리 곱해줘야 그만큼의 갯수가 나온다.
    # if문을 나오면 해당 합의 중복이 제외된다.

    elif tmp < s:
        lp += 1
    else:
        rp -= 1

# 1 빼야함 왜? --> (조합의 특징) 공..
print(ans-1 if s == 0 else ans)

###################33###################33###################33###################33
# 부분수열의 합 딕셔너리 버전 위 보다 느림..

from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = arr[:n//2], arr[n//2:]

l_sum, r_sum = dict(), dict()
count = 0
for i in range(n//2+1):
    cm = combinations(left, i)
    for c in cm:
        sm = sum(c)
        if l_sum.get(sm):
            l_sum[sm] += 1
        else:
            l_sum[sm] = 1

for i in range(n - n//2 + 1):
    cm = combinations(right, i)
    for c in cm:
        sm = sum(c)
        if r_sum.get(sm):
            r_sum[sm] += 1
        else:
            r_sum[sm] = 1

result = 0
for dic in l_sum:
    if r_sum.get(s-dic):
        result += r_sum[s-dic] * l_sum[dic]

print(result - 1 if s == 0 else result)