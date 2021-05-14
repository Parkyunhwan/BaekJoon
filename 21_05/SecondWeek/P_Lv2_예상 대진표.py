def solution(n, a, b):
    answer = 1
    if a > b:
        a, b = b, a

    i = 1
    while a + 1 != b:
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        val = pow(2, i)
        a //= val
        b //= val
        i += 1

    return i