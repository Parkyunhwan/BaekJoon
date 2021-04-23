N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
m_ab = []
for _ in range(M):
    m_ab.append(list(map(int, input().split())))

hap = [0] * (N + 1)
sm = 0
for i in range(1, N + 1):
    sm += arr[i]
    hap[i] = sm

for val in m_ab:
    a, b = val
    partition_sum = hap[b] - hap[a - 1]
    print(partition_sum)
