# https://suri78.tistory.com/26
# 해당 문제 티스토리 읽고 정리하기

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

min = arr[0][1] # 끝나는 최소 시각 저장
arr = arr[1:]
count = 1
for start, end in arr:
    if start >= min:
        min = end
        count += 1

print(count)