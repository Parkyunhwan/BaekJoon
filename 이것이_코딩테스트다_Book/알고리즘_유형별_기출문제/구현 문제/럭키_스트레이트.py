# https://www.acmicpc.net/problem/18406

n = list(map(int, list(input())))
length = len(n)
l_sum = sum(n[:length//2])
r_sum = sum(n[length//2:])

if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")