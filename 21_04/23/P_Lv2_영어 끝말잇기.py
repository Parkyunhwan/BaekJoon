def solution(n, words):
    answer = []
    set_word = set()
    idx = 1
    game_num = 1
    flag = False
    prev_word = words[0][0]
    for word in words:
        if word in set_word or prev_word[-1] != word[0]:
            print(word, prev_word[-1], word[0])
            flag = True
            break
        set_word.add(word)
        idx += 1
        prev_word = word
        if idx == n + 1:
            idx = 1
            game_num += 1

    if flag:
        return [idx, game_num]
    else:
        return [0, 0]

    return answer

'''
    다른사람 코드...
    
    1. 시작점과 끝 부분이 같은 지 비교
    2. 현재워드가 현재까지 워드들 사이에 포함되는지 검사
    
    3. 현재 index번호는 실행한 횟수를 사람수로 나눈 나머지 + 1 이다.
    4. 현재 차수는 실행한 횟수를 사람수로 나눈 횟수 + 1 이다.
'''
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]