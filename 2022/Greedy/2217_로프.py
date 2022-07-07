N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort(reverse=True)
result = 0
tmp_li = []
min_value = 1e9
for count in range(1, N + 1):
    min_value = min(min_value, num[count - 1]) # 해당라인은 지워도됨 -> 어차피 정렬해서 이후에 나오는 값이 현재보다 작으므로
    result = max(count * min_value, result)
print(result)

'''
최대 무게가 가장 큰 로프가 무게를 분산시킨다고 하더라도 가장 잘 버티므로 항상 먼저 올 수 있다. 
하지만 로프들이 버틸 수 있는 최대 무게는 (현재 사용중인 로프 중에서 9가장 약한 로프의 최대 무게 * 분산갯수) 이다.

그러므로 그리디하게 가장 잘 버티는 로프 부터 갯수를 늘려가면 된다.
'''