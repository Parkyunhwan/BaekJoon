N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# sorted(arr, key=lambda x:x[1])
arr = sorted(arr, key=lambda x:(x[1], x[0])) # 끝나는 시간 + 시작 시간을 정렬해야함
# (2, 2) , (1, 2)의 경우 2, 2가 적용된 후에도 1, 2가 들어올 수 있게 되어버린다.
# 따라서 반드시 시작 시간이 빠른 것부터 들어와야한다.


curr_time = 0
count = 0
for val in arr:
    start, end = val
    if start >= curr_time:
        count += 1
        curr_time = end

print(count)