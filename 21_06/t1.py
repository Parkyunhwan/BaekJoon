def solution(students):
    answer = []

    for idx, student in enumerate(students):
        score = 10
        late_num = 0
        absent_num = 0
        flag_absent = False
        for state in student:
            if state == 'A':
                score += 1
            elif state == 'L':
                late_num += 1
                if late_num == 3:
                    absent_num += 1
                    late_num = 0
            elif state == 'P':
                score -= 1
                absent_num += 1

            if absent_num == 3:
                flag_absent = True
                break

        if flag_absent:
            answer.append((0, idx + 1))
        else:
            answer.append((score, idx + 1))

    answer = sorted(answer, reverse=True, key = lambda x : (x[0], -x[1]))
    answer = [a[1] for a in answer]

    return answer