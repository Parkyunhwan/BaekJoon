# https://stricky.tistory.com/155
n = int(input())

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos) # 가장 큰 원반을 뺀 모든 원반을 from에서 aux로 이동
    print(from_pos, "->", to_pos) # 가장 큰 원반을 from -> to로 이동
    hanoi(n - 1, aux_pos, to_pos, from_pos) # aux의 원반들을 모두 to로 이

hanoi(n, 1, 3, 2)