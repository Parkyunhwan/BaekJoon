# 1회차 -> x : 너무 어려움, 아예 이해 못함

from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    mn = len(dist) + 1

    for start in range(length):  # 시작위치 선정
        for per in list(permutations(dist, len(dist))):  # 친구 순서 정하기
            count = 1
            distance = weak[start] + per[count - 1]
            if distance == 16:
                print(1)
            for i in range(start, start + length):
                if distance < weak[i]:
                    if weak[start] == 9:
                        print(distance, weak[i], start, i, start + length)
                    count += 1
                    if count > len(dist):
                        break
                    distance = weak[i] + per[count - 1]
            mn = min(mn, count)
    if mn > len(dist):
        return -1
    return mn