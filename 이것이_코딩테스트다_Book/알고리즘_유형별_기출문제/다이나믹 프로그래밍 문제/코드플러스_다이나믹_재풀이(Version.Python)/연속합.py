n = int(input())
num_list = list(map(int, input().split()))
temp = [0 for _ in range(n)]
result = -1001

for i in range(n):
    temp[i] = max(temp[i - 1] + num_list[i], num_list[i])
    result = max(result, temp[i])

print(result)