'''
    반복 풀이 (3)
    https://sihyungyou.github.io/baekjoon-12015/

'''
import bisect
N = int(input())
dp = [0] * (N + 1)
arr = [0] + list(map(int, input().split()))

bise = []
result = 0
cnt = 0
for i in range(1, N + 1):
    if not bise:
        bise.append(arr[i])
        cnt += 1
    else:
        if bise[-1] < arr[i]:
            bise.append(arr[i])
            cnt += 1
        else:
            idx = bisect.bisect_left(bise, arr[i]) # 내가 들어갈 위치를 찾음
            bise[idx] = arr[i] # 내가 들어가도 증가하는 수열의 조건이 유지됨.

print(cnt)