n = int(input())
arr = list(map(int, input().split()))

mx = 0


def dfs(arr: list, energy):
    global mx

    if len(arr) <= 2:
        mx = max(mx, energy)
        return

    for i in range(1, len(arr) - 1):
        w_energy = arr[i - 1] * arr[i + 1]
        val = arr.pop(i)
        dfs(arr, energy + w_energy)
        arr.insert(i, val)

dfs(arr, 0)
print(mx)