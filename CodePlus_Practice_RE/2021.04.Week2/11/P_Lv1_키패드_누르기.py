def solution(numbers, hand):
    answer = []
    l_hand = [3, 0]
    r_hand = [3, 2]
    left = [1, 4, 7]
    right = [3, 6, 9]
    for number in numbers:
        if number == 0:
            number = 11
        num = number - 1
        if number in left:
            answer.append('L')
            l_hand = [num // 3, num % 3]
        elif number in right:
            answer.append('R')
            r_hand = [num // 3, num % 3]
        else:
            x, y = num // 3, num % 3
            diff_l = abs(x - l_hand[0]) + abs(y - l_hand[1])
            diff_r = abs(x - r_hand[0]) + abs(y - r_hand[1])
            print(number)
            print(l_hand, r_hand, diff_l, diff_r)
            if diff_l > diff_r:
                answer.append('R')
            elif diff_l < diff_r:
                answer.append('L')
            else:
                answer.append(hand[0].upper())

            if answer[-1] == 'R':
                r_hand = [num // 3, num % 3]
            else:
                l_hand = [num // 3, num % 3]
    return ''.join(answer)