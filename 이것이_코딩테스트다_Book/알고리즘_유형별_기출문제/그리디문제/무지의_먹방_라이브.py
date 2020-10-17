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