import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

chi = []
home = []


def get_distance(p):
    city_dist = 0
    for h in home:
        hx, hy = h[0], h[1]
        chiken_dist = int(1e9)
        for p_com in p:
            px, py = p_com
            dist = abs(hx-px) + abs(hy-py)
            chiken_dist = min(dist, chiken_dist)

        city_dist += chiken_dist
    return city_dist


def solution(arr, n, m):
    min_value = int(1e9)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                chi.append((i, j))
            elif arr[i][j] == 1:
                home.append((i, j))

    for per in list(combinations(chi, m)): # m개 치킨집고르기
        distance = get_distance(per)
        min_value = min(min_value, distance)

    return min_value


print(solution(a, n, m))