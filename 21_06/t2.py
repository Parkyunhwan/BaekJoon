def solution(drum):
    answer = 0

    for y in range(len(drum)):
        x = 0

        star = 0
        flag = False

        while True:
            if drum[x][y] == '#':
                x += 1
            elif drum[x][y] == '>':
                y += 1
            elif drum[x][y] == '<':
                y -= 1
            elif drum[x][y] == '*':
                star += 1
                x += 1
                if star == 2:
                    break

            if x == len(drum):
                flag = True
                break

        if flag:
            answer += 1
    return answer