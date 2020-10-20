# 1회차 실패 ->

# !! 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적해를 보장하므로 `그리디 알고리즘`으로 볼 수 있다.
# 정렬 후 숫자를 무작정 오름차순으로 더하는 것이 아니다.
# 더하다 보면 숫자의 크기가 역전되기 때문이다.

# 따라서, heap을 이용해서 항상 최솟값을 뽑아줄 수 있도록 한다.
# 여기서 주의할 점은 두개를 뽑아 한개를 heap에 삽입하므로 heap에 남은 갯수가 1개일때 멈춰야만 한다.
import heapq

heap = []
n = int(input())
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

sm = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sm += one + two
    heapq.heappush(heap, one+two)

print(sm)



### 틀린코드
# n = int(input())
# arr = [int(input()) for _ in range(n)]
#
# arr.sort()
# sm = arr[0] + arr[1]
# tmp = sm
# for i in range(2, len(arr)):
#     tmp = tmp + arr[i]
#     sm += tmp
# print(sm)
