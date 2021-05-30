'''
    'tanks 범위 조건 10만'

    즉, O(n^2) 는 안되고 최대 O(nlogn)까지 가능한 문제
    따라서, heapq를 이용해 logn만에 최댓값과 최소인덱스를 찾음
'''
import heapq

def solution(tanks):
    flag = False
    q = []
    for idx, tank in enumerate(tanks):
        heapq.heappush(q, [-tank, idx])


    while True:
        for idx, tank in enumerate(tanks):
            if tank <= 0:
                continue
            if len(q) == 1:
                flag = True
                break
            value = heapq.heappop(q)
            score, score_idx = -value[0], value[1]
            if score_idx == idx:
                value2 = heapq.heappop(q)
                score, score_idx = -value2[0], value2[1]
                heapq.heappush(q, value)

            tanks[score_idx] -= (tank * 2)
            if tanks[score_idx] > 0:
                heapq.heappush(q, [-tanks[score_idx], score_idx])

        if flag:
            break

    return q[0][1]