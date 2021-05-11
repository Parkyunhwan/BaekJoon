def solution(record):
    answer = []
    dic = dict()
    record_arr = []
    for rec in record:
        rec = rec.split(" ")
        record_arr.append([rec[0], rec[1]])
        if len(rec) > 2:
            dic[rec[1]] = rec[2]

    for rec in record_arr:
        action, uid = rec
        if action == 'Enter':
            answer.append(dic[uid] + "님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(dic[uid] + "님이 나갔습니다.")

    return answer