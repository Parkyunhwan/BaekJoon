'''
    `시간 초과` 문제

    입력 값을 '최대힙', '최소힙'에 둘다 삽입한 후 한쪽에서 삭제 시 다른 한쪽의 값을 찾아 삭제하면 추가로 n^2이 걸릴 수 있다.
    따라서, 시간초과가 발생한다.

    %어떻게 시간을 줄일 수 있을까?%

        * 유효성 검사 *
        유효성 검사 배열을 만든다.

        입력 값을 양쪽에 넣고 해당 인덱스를 유효한 값으로 표시한다. (값을 유효하게 하면 중복값을 처리할 수 없다)

        1. 한쪽 힙에서 삭제되었다면 '유효성 배열'에서 해당 인덱스를 무효로 표시하고 넘어간다. (바로 삭제 x)
        2. 1번을 하기전에 꼭 검사해줘야한다.
            * 현재 큐의 top값의 인덱스가 유효하지 않다면 유효한 인덱스가 나올 때 까지 힙을 pop한다.
            * 유효한 인덱스를 만나거나 힙이 없다면 반복을 종료하고 1번을 실행한다.

        2번을 통해 1번에선 유효한 인덱스를 큐에서 뺄 수 있게 되었다.

        시간복잡도는 O(nlogn)
'''
import heapq
T = int(input())

min_q = []
max_q = []

for _ in range(T):
    K = int(input())
    visited = [False] * (1000000 + 1)
    for i in range(K):
        val = list(input().split())
        oper, num = val[0], int(val[1])
        if oper == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = True # 현재 인덱스를 유효한 인덱스로 표시
        elif oper == 'D':
            if num == 1:
                while max_q: # 유효하지 않은 값이 위에 있다면 제외
                    curr_num, curr_idx = heapq.heappop(max_q)
                    if visited[curr_idx]:
                        heapq.heappush(max_q, (curr_num, curr_idx))
                        break
                if max_q: # 유효한 값이 있나? 그럼 빼야지
                    curr = heapq.heappop(max_q)
                    curr_num, curr_idx = curr
                    visited[curr_idx] = False
            else:
                while min_q:  # 유효하지 않은 값이 위에 있다면 제외
                    curr_num, curr_idx = heapq.heappop(min_q)
                    if visited[curr_idx]:
                        heapq.heappush(min_q, (curr_num, curr_idx))
                        break
                if min_q:  # 유효한 값이 있나? 그럼 빼야지
                    curr = heapq.heappop(min_q)
                    curr_num, curr_idx = curr
                    visited[curr_idx] = False

    while max_q:  # 유효하지 않은 값이 위에 있다면 제외
        curr_num, curr_idx = heapq.heappop(max_q)
        if visited[curr_idx]:
            heapq.heappush(max_q, (curr_num, curr_idx))
            break
    while min_q:  # 유효하지 않은 값이 위에 있다면 제외
        curr_num, curr_idx = heapq.heappop(min_q)
        if visited[curr_idx]:
            heapq.heappush(min_q, (curr_num, curr_idx))
            break

    if min_q and max_q:
        print("%d %d" %(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0]))
    else:
        print("EMPTY")

# 시간초과 실패 코드
'''
import heapq
T = int(input())

min_q = []
max_q = []
for _ in range(T):
    for i in range(int(input())):
        val = list(input().split())
        oper, num = val[0], int(val[1])
        if oper == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
        elif oper == 'D':
            if not min_q:
                continue
            if num == 1:
                curr = heapq.heappop(max_q)
                curr *= -1
                idx = min_q.index(curr)
                del min_q[idx]
            else:
                curr = heapq.heappop(min_q)
                idx = max_q.index(-curr)
                del max_q[idx]

    if min_q:
        print("%d %d" %(-heapq.heappop(max_q), heapq.heappop(min_q)))
    else:
        print("EMPTY")
'''