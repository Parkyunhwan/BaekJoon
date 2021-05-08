def solution(s):
    answer = ""
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    tmpword = ""
    for i in range(len(s)):
        if s[i].isdigit():
            if len(tmpword) != 0:
                answer = answer + dic[tmpword]
                # print(dic[tmpword], end='')
                tmpword = ""
            answer = answer + s[i]
            # print(s[i], end='')
        else:
            tmpword = tmpword + s[i]
            if tmpword in dic:
                answer = answer + dic[tmpword]
                # print(dic[tmpword], end='')
                tmpword = ""

    return answer


print(solution("one4seveneight"))