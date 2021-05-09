'''
    내풀이

'''
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        flag = False
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
        for val in scoville:
            if val >= K:
                continue
            else:
                flag = True
                break
        if not flag:
            return answer

    return -1


import heapq as hq

'''
    다른사람의 정말 군더더기 없는 코드...
'''
def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer