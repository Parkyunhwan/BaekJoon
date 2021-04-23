'''
    최대공약수 구할 때
    큰값이 작은 값이 되고
    작은 값은 나머지 값이 된다.

    (반복)

'''
a, b = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def gcd_while(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b, c):
    return a * b // c


if a < b:
    a, b = b, a
gcd_value = gcd(a, b)
print(gcd_value)
print(lcm(a, b, gcd_value))