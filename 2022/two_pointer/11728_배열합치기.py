a, b = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
result = []
i, j = 0, 0

a_poi, b_poi = 0, 0
a_len, b_len = a, b

while a_poi != a_len or b_poi != b_len:
    if a_poi == a_len:
        result.append(b_list[b_poi])
        b_poi += 1
    elif b_poi == b_len:
        result.append(a_list[a_poi])
        a_poi += 1
    else:
        if a_list[a_poi] < b_list[b_poi]:
            result.append(a_list[a_poi])
            a_poi += 1
        else:
            result.append(b_list[b_poi])
            b_poi += 1

print(*result)