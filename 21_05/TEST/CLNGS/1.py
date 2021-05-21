def solution(price, money, count):
    need = price * (count + 1) * count // 2
    diff = need - money
    if diff <= 0:
        return 0
    else:
        return diff