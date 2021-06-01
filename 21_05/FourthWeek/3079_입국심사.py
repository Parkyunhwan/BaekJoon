'''
    문제만 봐서 '이분 탐색'을 어떻게 사용해야할 지 감을 잡기 어려운 문제

    문제에서 이분 탐색이라는 포인트를 잡았다면 문제를 풀기 쉬웠을 것 같다.

    -> 먼저 X 시간이라고 답을 가정하고 풀고 만약 X 시간 보다 긴 시간이 필요하다면 이분 탐색으로 그 윗값을 선택하고
    짧은 시간이 필요하다면 이분 탐색으로 그 아랫값을 선택하도록 한다.

'''
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

mx = max(arr)
left, right = 1,  mx * M
ans = 0

while left <= right:
    mid = left + (right - left) // 2

    sm = 0
    for i in range(N):
        sm += mid // arr[i]

    if sm < M:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1


print(ans)