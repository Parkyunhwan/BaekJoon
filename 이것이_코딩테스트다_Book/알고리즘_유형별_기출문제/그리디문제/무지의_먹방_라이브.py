# 그리디 문제는 생각하는 과정이 필요하다. 설계가 먼저 제대로 되야 좋은 코드를 짤 수 있다.
# 시간이 적게 걸리는 요소부터 0으로 만들어가는 시간을 측정하며 0으로 만들 수 없을 때까지 시간을 구하고
# 남은 시간 만큼 요소를 이동한 인덱스를 출력하도록 한다.
import heapq


def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

# 2회차 시 (가장 작은 숫자를 기준으로 한바퀴가 돈다는 것을 기억하자)
# 시간을 1씩 증가시키면서 하나씩 빼면서 0이되는 숫자를 찾는 것은 k만큼의 시간이 걸린다. (효율성 10^3^13)이므로 절대 불가
# 가장 작은 숫자를 선택해서 그 숫자를 빼는 방식을 사용하면 매번 food_times(20만)만큼 빼야한다. 20만 * 20만 = 40,000,000,000
# 가장 작은 숫자를 선택해서 그 음식을 모두 먹는데 걸리는 시간이 k를 넘지 않는다면 시간을 추가하고
# k를 넘는다면 나머지를 구해 남은 시간까지 해당하는 음식의 위치에서 남은 음식의 양을 출력합니다.
# food_times	k	result
# [3, 1, 2]	5	1

import heapq

def solution2(food_times, k):
    length = len(food_times)
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    previous = 0
    sum_value = 0
    while sum_value + (q[0][0]-previous)*length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]