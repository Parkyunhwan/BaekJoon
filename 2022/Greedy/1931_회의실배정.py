N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : (x[1], x[0]))

start_time = 0
end_time = 0
count = 0
for i in range(len(arr)):
    curr_start_time = arr[i][0]
    curr_end_time = arr[i][1]
    if curr_start_time >= end_time:
        start_time = curr_start_time
        end_time = curr_end_time
        count += 1

print(count)

# 한회의가 끝나는 동시에 다음 회의가 시작될 수 있다는 조항 (finalEnd == start)가 같아도 된다.
# 회의의 시작시간과 끝나는시간이 동일할 수 있다는 조항 (2, 2), (1, 2)의 경우에 (2, 2)를 먼저체크하면 (1, 2)는 체크될 수 없다.
