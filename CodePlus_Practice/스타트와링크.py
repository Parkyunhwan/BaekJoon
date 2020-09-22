# https://hwiyong.tistory.com/307
# velog
from itertools import combinations

N = int(input())
board = []
for _ in range(N):
    # map을 이용하여 split한 문자열을 int형으로 변환하고 list에 넣는다.
    board.append(list(map(int,input().split())))

num_list = list(range(N)) # 0~N-1 까지의 숫자를 리스트로 만듬

res = float('inf') # min 초기 값 지정할 때 매우 유용

def solve():
    global res # res는 이제 global변수를 사용함

    for cand in combinations(num_list,N//2): # 리스트에서 반절을 뽑음

        start_mem = list(cand) # 반절 그대로 가져감
        link_mem = list(set(num_list) - set(cand)) # 반절 남은 거 가져감

        start_comb = list(combinations(start_mem,2)) # 반절에서 2개를 뽑은 리스트
        link_comb = list(combinations(link_mem, 2))

        start_sum = 0
        for x, y in start_comb: # 반절에서 2개씩 뽑은 리스트 반복
            start_sum += (board[x][y] + board[y][x]) # 총합을 구함

        link_sum = 0
        for x, y in link_comb:
            link_sum += (board[x][y] + board[y][x])

        res = min(res, abs(start_sum - link_sum)) # 최솟값을 구함
    # 조합을 바꿔가며 반복
solve()
print(res)
# time over
# import itertools
#
# num = int(input())
# li = []
# for _ in range(num):
#     s = list(map(int,input().split()))
#     li.append(s)
#
# n = []
# for i in range(num):
#     if i < num/2:
#         n.append(0)
#     else:
#         n.append(1)
#
# n = set(itertools.permutations(n))
#
# mn = 999999999
#
# for comp in n:
#     start = []
#     link = []
#     for i,c in enumerate(comp):
#         if c==0:
#             start.append(i)
#         else:
#             link.append(i)
#     start_sum = 0
#     link_sum = 0
#     for i in range(num//2):
#         for j in range(i+1,num//2):
#             start_first = start[i]
#             start_second = start[j]
#
#             start_sum += li[start_first][start_second] + li[start_second][start_first]
#
#             link_first = link[i]
#             link_second = link[j]
#
#             link_sum += li[link_first][link_second] + li[link_second][link_first]
#
#     mn = min(mn, abs(start_sum-link_sum))
#
# print(mn)

