import itertools

def dfs(arr, index, result):
    if len(result) == 6:
        for val in result:
            print(val, end=' ')
        print()
        return
    for i in range(index, len(arr)):
        result.append(arr[i])
        dfs(arr, i + 1, result)
        result.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    arr = arr[1:]
    if k == 0:
        break
    result = []
    dfs(arr, 0, result)
    print()

