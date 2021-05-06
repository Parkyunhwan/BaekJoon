'''
    우선순위큐를 이용해 중간값 찾기..

    '중간값 구하기 알고리즘'
    https://www.crocus.co.kr/625


'''
import heapq
N = int(input())
arr = [int(input()) for _ in range(N)]

max_heap = []
min_heap = []
for i in range(N):
    len_max_heap = len(max_heap)
    len_min_heap = len(min_heap)

    if len_max_heap == len_min_heap:
        heapq.heappush(max_heap, -arr[i])
    else:
        heapq.heappush(min_heap, arr[i])
    if min_heap and max_heap:
        if -max_heap[0] > min_heap[0]:
            mx = -heapq.heappop(max_heap)
            mn = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -mn)
            heapq.heappush(min_heap, mx)
    print(-max_heap[0])

