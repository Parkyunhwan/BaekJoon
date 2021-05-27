import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

num = 0
for val in A:
    val = val - B # 음수가 될 수도 있으므로 예외 처리가 필요하다.
    num += 1
    if val > 0:
        val = val / C
        val = math.ceil(val)
        num += int(val)
print(num)