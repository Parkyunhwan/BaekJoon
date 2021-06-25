import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr_n = set()
for _ in range(N):
    arr_n.add(input().rstrip()) # 리스트 대신 세트를 사용

result = 0
for _ in range(M):
    str = input().rstrip()
    if str in arr_n: # 이미 있는 문자 체크가 세트가 리스트보다 빠르기에 시간초과가 나지 않았음
        result += 1

print(result)