'''
    그리디 문제

    문제를 무조건 그리디이다 증명하긴 어렵지만

    시간이나 여러가지 케이스를 시도했을 때 그리디 예상.
'''
def solution(goal):
    answer = 0
    arr = [0] * len(goal)

    for idx, val in enumerate(goal):
        save = arr[idx]
        answer += abs(val - arr[idx])
        for i in range(idx, len(goal)):
            arr[i] += (val - save)

    return answer