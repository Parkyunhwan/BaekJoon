# 범위 문제에선 뭔가 확장하는 테크닉이 많은 것 같다.
# 회전 후 모든 시작 위치에 대해 자물쇠를 끼워 맞춰 합을 구하는 것이 중요했다.

def rotation_90_degree(arr):
    li = []
    for j in range(len(arr)):
        tmp = []
        for i in range(len(arr) - 1, -1, -1):
            tmp.append(arr[i][j])
        li.append(tmp)
    return li


def check(arr):
    length = len(arr) // 3
    for i in range(length, 2 * length):
        for j in range(length, 2 * length):
            if arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    key_l = len(key)
    lock_l = len(lock)

    new_lock = [[0] * (lock_l * 3) for _ in range(lock_l * 3)]

    for i in range(lock_l):
        for j in range(lock_l):
            new_lock[lock_l + i][lock_l + j] = lock[i][j]

    for _ in range(4):
        key = rotation_90_degree(key)
        for x in range(2 * lock_l):
            for y in range(2 * lock_l):
                # x, y 시작 위치
                for i in range(key_l):  # key의 길이만큼
                    for j in range(key_l):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True

                for i in range(key_l):
                    for j in range(key_l):
                        new_lock[x + i][y + j] -= key[i][j]
    return False