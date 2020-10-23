n = int(input())
# 분 하나 당 -> 3 13 23 33 43 53 -> 6개 단, 30 .. 39 10개 => 16-1 = 15
# 시간 당 분 -> 3 13 23 33 43 54 -> 6개 에선 모든 초가 참; 30..39에서 모든 초가 참 -> 15 * 59
# 시간이 3 일 때 -> 모든 분 과 초가 참 59 * 59 -- > 복잡한 규칙 찾기 xxxxx 좋지 않음)
# __________

# 간단하게 완전탐색으로 풀면된다. -> 총 검사해야 할 갯수는 60 * 60 * (n+1) 개 이기 때문이다. 최대 갯수는 24*60*60  < 100000 개 이하이다.
hour, minute, second = 0, 0, 0
count = 0
while True:
    if '3' in str(hour)+str(minute)+str(second):
        count += 1
    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == n+1:
        break
print(count)

# 시간 문제는 구현 문제에서 많이 나오는 편이다. 시간은 계속흐르므로 for문으로 하나씩 검사할 수 있다.
h = int(input())
count = 0
for i in range(h+1):  # hour
    for j in range(60):  # minute 0 ~ 59
        for k in range(60):  # second 0 ~ 59
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)