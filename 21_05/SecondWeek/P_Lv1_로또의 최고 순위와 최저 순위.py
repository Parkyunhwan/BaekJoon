def solution(lottos, win_nums):
    answer = []
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    count = 0
    for lotto in lottos:
        if lotto in win_nums:
            if lotto not in answer:
                answer.append(lotto)
        elif lotto == 0:
            count += 1
    mn = len(answer)
    mx = len(answer) + count
    print(mn, mx)
    if mn < 2:
        mn = 6
    else:
        mn = dic[mn]

    if mx < 2:
        mx = 6
    else:
        mx = dic[mx]
    answer = [mx, mn]
    return answer