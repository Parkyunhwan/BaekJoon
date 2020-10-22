# 1회차 -> 손도 못댐.. < 가장 인접한 두 공유기 사이의 거리를 최대로 하는 값 > 이 어떻게 구해지지??
# -> 이것은 모든 공유기들의 사이 간격이 공평하게 설치되기를 바라는 것을 의미한다고 볼 수 있다.
#
# 출처: https://mygumi.tistory.com/301 [마이구미의 HelloWorld]
# 이진 탐색으로 간격을 정해가면서 전체 공유기가 모두 들어가면 기록하고 더 큰 간격을 찾고
# 전체 공유기가 들어가지 못하면 간격을 줄여 전체 공유기가 들어가도록 하게 한다.

# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
     array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(Gap)을 의미
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치하기
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)