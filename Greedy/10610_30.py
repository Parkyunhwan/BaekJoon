n = list(map(int, list(input())))
n.sort(reverse=True)

sm = sum(n)

if 0 not in n or sm % 3:
    print(-1)
    exit(0)
n = list(map(str, n))
print(''.join(n))


