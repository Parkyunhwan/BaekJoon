import sys
N = int(input())
arr = list(map(int, input().split()))

arr.sort()
i = 0
j = len(arr) - 1

min_value = sys.maxsize
result = [-1, -1]
while i < j:  # 한 배열에서 투포인터 종료 지점은 두 인덱스가 교차할 때
    sm = arr[i] + arr[j]
    if abs(min_value) > abs(sm):
        result = [arr[i], arr[j]]
        min_value = sm
        if sm == 0:
            break
    if sm < 0:
        i += 1
    elif sm > 0:
        j -= 1

for r in result:
    print(r, end=' ')
