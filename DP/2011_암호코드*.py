n = input()
dp = [0] * 5001

if n[0] == '0':
    print(0)
    exit(0)

dp[0] = dp[1] = 1

for i in range(2, len(n) + 1):
    a = n[i - 1]
    b = n[i - 2]
    if a == '0' and b == '0':
        print(0)
        exit(0)
    if a != '0':
        dp[i] += dp[i - 1] # 한자리 숫자
    if b != '0':
        num = int(b) * 10 + int(a)
        if num <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000
print(dp[len(n)])