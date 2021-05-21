def solution(h, w, blocks):
    answer = []
    blocks = sorted(blocks, key=lambda x : (x[1], x[0])) # (행, 열) 순서로 오름차순 정렬

    bj = 0
    curr = 0
    prev = [-1, -1]

    for i in range(h): # 모눈종이의 각 행을 돌면서 검사
        count = 0
        while bj < len(blocks):
            if blocks[bj][1] == i: # 현재 행과 같은 행의 block일 때만
                if prev != blocks[bj]: # 이전과 같은 좌표라면 겹치는 블록이므로 넘어감
                    count += 1 # black 추가
                    prev = blocks[bj]
            else:
                break
            bj += 1
        ret = w - count # 각 행의 blue block 갯수 구함
        curr += ret
        answer.append(curr)
    return answer