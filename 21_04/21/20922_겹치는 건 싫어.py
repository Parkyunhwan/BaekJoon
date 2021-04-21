from collections import defaultdict
N, K = map(int, input().split())

arr = list(map(int, input().split()))

dic = defaultdict(int)
i = 0
j = 0
max_length = 0
while j < len(arr):
    if dic[arr[j]] < K:
        dic[arr[j]] += 1
        j += 1
        if max_length < j - i:
            max_length = j - i
    else:
        dic[arr[i]] -= 1
        i += 1

print(max_length)