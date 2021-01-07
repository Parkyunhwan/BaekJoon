t = int(input())


def gcd(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def lcm(m, n):
    return m * n / gcd(m, n)


for _ in range(t):
    m, n ,x, y = map(int, input().split())
    x -= 1
    y -= 1
    tmp_x, tmp_y = 0, 0
    last = int(lcm(m, n))
    flag = False
    for i in range(0, last + 1, m):
        tmp_x = x
        tmp_y = (i + x) % n
        if tmp_x == x and tmp_y == y:
            flag = True
            print(i + x + 1)
            break
    if flag is False:
        print(-1)