'''
    효율성 문제...(좋은 문제인것 같다 **두개)

    효율성 문제를 해결할 수 있는 3가지 방법

    1. 투 포인터
    2. 슬라이딩 윈도우
    3. 이분 탐색

    ....스택사용, 우선순위 큐(그리디) 등등

    https://covenant.tistory.com/162
'''
def solution(stones, k):
    answer = 0

    left = 1
    right = 200000000

    while left <= right:
        mid = (right + left) // 2
        count = 0
        max_count = -1

        for val in stones:
            if val - mid <= 0:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        max_count = max(count, max_count)

        if max_count >= k:
            right = mid - 1
        elif max_count < k:
            left = mid + 1

    return left