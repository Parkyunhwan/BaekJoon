# 1회차 실패
# 정렬한 배열의 한 가운데 값이
# 어떤 한점에서 모든 점으로의 거리의 최솟값이다.
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[(n-1)//2])