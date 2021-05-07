'''
    중복 순열 문제

'''
num = []
select = []
count = 0
set1 = set()

def check(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True  # 소수


def dfs(i, val):
    global count
    if i == len(num) + 1:
        return
    if len(val) != 0 and int(val) not in set1 and check(int(val)):
        set1.add(int(val))
        count += 1

    for idx in range(len(num)):
        if not select[idx]:
            select[idx] = True
            dfs(i + 1, val + num[idx])
            select[idx] = False


def solution(numbers):
    global num, select
    num = numbers
    select = [False] * len(num)
    answer = 0
    dfs(0, "")
    return count