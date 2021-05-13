def solution(s):
    answer = len(s)

    # 압축 단어 길이
    for comp_len in range(1, len(s) // 2 + 1):
        compress_word = ""
        i = 0
        curr_word = ""
        count = 1

        while i < len(s):
            temp = s[i:i + comp_len]
            if curr_word == temp:
                count += 1
            else:
                if count == 1:
                    compress_word += curr_word
                elif count > 1:
                    compress_word += (str(count) + curr_word)
                count = 1
                curr_word = temp
            i += comp_len

        if count > 1:
            compress_word += str(count)
        compress_word += curr_word
        answer = min(answer, len(compress_word))
        print(compress_word)
    return answer

print(solution("abcabcdede"))