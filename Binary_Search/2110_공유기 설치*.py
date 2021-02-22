# https://assaeunji.github.io/python/2020-05-07-bj2110/
n, c = map(int, input().split())

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 가장 낮은 좌표와 그 다음으로 낮은 좌표의 차이
start = house[1] - house[0]
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start + end) // 2  # 해당 gap
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:  # gap 이상
            count += 1
            old = house[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)