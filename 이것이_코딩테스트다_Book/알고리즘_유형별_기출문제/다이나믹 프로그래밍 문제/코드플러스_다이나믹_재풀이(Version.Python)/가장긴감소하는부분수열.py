n = int(input())
lst = list(map(int, input().split())) 
dp = [1 for i in range(n)] # 자기 자신은 기본적으로 포함하고 있으므로 초깃값을 1로 설정한다.
for i in range(n):
    for j in range(i): 
        if lst[i] < lst[j]: 
            dp[i] = max(dp[i], dp[j] + 1) 
print(max(dp))
