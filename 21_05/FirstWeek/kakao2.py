def valid_place(place):
    for i in range(len(place)):  # 5
        for j in range(len(place[i])):  # 5
            if place[i][j] == 'P':
                partition1 = False
                partition2 = False
                partition3 = False
                partition4 = False
                if i + 1 < 5:
                    if place[i + 1][j] == 'X':
                        partition1 = True
                    elif place[i + 1][j] == 'P':
                        return 0
                if j + 1 < 5:
                    if place[i][j + 1] == 'X':
                        partition2 = True
                    elif place[i][j + 1] == 'P':
                        return 0

                if i - 1 >= 0:
                    if place[i - 1][j] == 'X':
                        partition3 = True
                    elif place[i - 1][j] == 'P':
                        return 0

                if j - 1 >= 0:
                    if place[i][j - 1] == 'X':
                        partition4 = True
                    elif place[i][j - 1] == 'P':
                        return 0

                # if partition1 and partition2: # 두 곳 모두 파티션이 있으므로 어차피 가능
                #     continue

                if i + 1 < 5 and j + 1 < 5 and place[i + 1][j + 1] == 'P':
                    if partition1 and partition2:
                        pass
                    else:
                        return 0

                if i + 1 < 5 and j - 1 >= 0 and place[i + 1][j - 1] == 'P':
                    if partition1 and partition4:
                        pass
                    else:
                        return 0

                if i - 1 >= 0 and j - 1 >= 0 and place[i - 1][j - 1] == 'P':
                    if partition3 and partition4:
                        pass
                    else:
                        return 0

                if i - 1 >= 0 and j + 1 < 5 and place[i - 1][j + 1] == 'P':
                    if partition2 and partition3:
                        pass
                    else:
                        return 0

                if not partition1 and i + 2 < 5 and place[i + 2][j] == 'P':
                    return 0
                if not partition2 and j + 2 < 5 and place[i][j + 2] == 'P':
                    return 0

                if not partition3 and i - 2 >= 0 and place[i - 2][j] == 'P':
                    return 0
                if not partition4 and j - 2 >= 0 and place[i][j - 2] == 'P':
                    return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(valid_place(place))
    print(answer)
    return answer

solution([["POOOP",
           "OOOOX",
           "OOOOP",
           "XPOOX",
           "POOXO"]])