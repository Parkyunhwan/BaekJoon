'''
    바같 반복문이 (전체 물품)이고
        이너 반복문이 (가방의 무게)인 이유

    하나의 물품에 대해 각 가방의 무게에 해당하는 최대 가치를 구해줘야한다.

    모든 물품이 가방의 무게에 적용되면 최댓값을 구할 수 있게된다.
'''
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

# bottom up2
for j in range(N):
    for k in range(K, 0, -1):
        w, v = arr[j]
        if k - w >= 0:
            dp[k] = max(dp[k], dp[k - w] + v)

print(max(dp))

'''
C++ bottom up1 

지금 현재 담을 수 없는 물품은 이전 무게 누적 최댓값으로 하고 넘어간다.
for (int i = 1; i <= N; i++) {
	for (int j = 1; j <= K; j++) {
				
		// i번째 무게를 더 담을 수 없는 경우 
		if(W[i] > j) {
			dp[i][j] = dp[i - 1][j];
		}
		// i번째 무게를 더 담을 수 있는 경우 
		else {
			dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]);
		}
				
	}
}
'''