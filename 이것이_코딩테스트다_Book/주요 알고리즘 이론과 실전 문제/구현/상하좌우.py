n = int(input())
direction = input().split()
sx, sy = 1, 1
for dir in direction:
    if dir == 'R':
        if sy + 1 >= n:
            continue
        else:
            sy += 1
    elif dir == 'L':
        if sy - 1 < 1:
            continue
        else:
            sy -= 1
    elif dir == 'U':
        if sx - 1 < 1:
            continue
        else:
            sx -= 1
    else:
        if sx + 1 >= n:
            continue
        else:
            sx += 1
print(sx, sy)

# 좀 더 콤팩트한 구현을 위해선 일반적으로 사용할 수 있게 만들어야 한다.
# dx, dy, move_types의 설정
# move_type에 따른 dx, dy의 변화