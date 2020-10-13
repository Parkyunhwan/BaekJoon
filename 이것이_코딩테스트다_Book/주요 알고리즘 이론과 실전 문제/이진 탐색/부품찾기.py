# 십만개의 숫자가 백만개 안에 있는지 1
# 한개 검사하는데 백만번 * 십만번 => 엄청큰 수 O(n*k) 불가능
# 하나검사하는데 log1000000 (백만 번) 20번 정도?
# 20 * 십만번 => 200만번
# -> 이진 탐색을 구현해서 구해야한다.


def binary_search(arr, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if arr[mid] == target:
        return "yes"
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)


n = int(input())
an = list(map(int, input().split()))
m = int(input())
bn = list(map(int, input().split()))
an.sort()
# bn.sort() 필요없
for b in bn:
    print(binary_search(an, b, 0, n-1), end=" ")



########################
# N(가게의 부품 개수) 입력
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')