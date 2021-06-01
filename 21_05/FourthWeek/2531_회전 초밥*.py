'''
    https://youseop.github.io/2020-11-04-%EC%98%A4%EB%8A%98%EC%9D%98-%EB%AC%B8%EC%A0%9C/
    ** 투 포인터 방식 풀이로 풀어보기 **
'''

N, d, k, c = map(int, input().split()) # 접시수, 초밥 가짓수, 연속 접시수, 쿠폰번호
arr = [int(input()) for _ in range(N)]

mx = 0
for i in range(N):
    if i + k <= N:
        set_arr = set(arr[i:i + k])
    else:
        remain = (i + k) % N
        set_arr = set(arr[i:i + k])
        set_arr2 = set(arr[:remain])
        set_arr = set_arr.union(set_arr2)
    count = len(set_arr)
    if c not in set_arr:
        count += 1
    mx = max(count, mx)

print(mx)


'''

'''
N, d, k, c = map(int, input().split()) # 접시수, 초밥 가짓수, 연속 접시수, 쿠폰번호
arr = [int(input()) for _ in range(N)]


mx = 0

for i in range(N):
    check = [False] * (d + 1)
    count = 0
    for j in range(i, i + k):
        if check[arr[j % N]]:
            continue
        else:
            check[arr[j % N]] = True
            count += 1
    if not check[c]:
        count += 1

    mx = max(mx, count)
print(mx)