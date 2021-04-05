n, k = map(int, input().split())

item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

item = [0] + item
dp = [0] * (k + 1)


def dps():
    for i in range(1, n + 1):
        for j in range(k, 0, - 1):
            if item[i][0] <= j:
                dp[j] = max(dp[j], dp[j - item[i][0]] + item[i][1])


dps()
print(dp[k])

'''
    D(i, k) i 번째 물건까지 사용하여 k 용량의 가방에 물건을 채울 때의 최대 가치
    N : 물건의 개수 
    K : 가방의 한계
    
    현재 i번째 물건일 때
    i번째 물건을 선택하지 않는 경우 vs i번째 물건을 선택하는 경우로 나눌 수 있다.
'''
