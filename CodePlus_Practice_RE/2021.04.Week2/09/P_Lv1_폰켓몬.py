# dict 풀이
from collections import defaultdict
def solution(nums):
    answer = 0
    count = defaultdict(int)
    n = 0
    for num in nums:
        if n == len(nums) // 2:
            break
        if count[num] != 0:
            continue
        count[num] += 1
        n += 1
    answer = len(count)
    return answer


# set 풀이법법 (중복값의 갯수를 하나로 만들어버리는 방법)
def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer