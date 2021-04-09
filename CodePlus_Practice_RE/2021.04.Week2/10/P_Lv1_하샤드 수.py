def solution(x):
    answer = True
    num = x

    val = []
    while num != 0:
        val.append(num % 10)
        num //= 10

    return True if x % sum(val) == 0 else False