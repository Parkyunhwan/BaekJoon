for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    x -= 1 # caculate easily
    y -= 1
    standard = x
    while standard < n * m:
        if standard % n == y:
            print(standard+1)
            break
        standard += m
    if standard % n != y:
        print(-1)





