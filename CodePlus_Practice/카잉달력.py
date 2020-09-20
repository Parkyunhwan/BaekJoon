for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k % n == y:
            print(k+1)
            break
        k += m
    if k % n != y:
        print(-1)