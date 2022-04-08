strs = input()
length = len(strs)
sorted_strs = sorted(strs)

result = [""] * length

def func(start, arr):
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[start + idx] = _min
    print(''.join(result))
    func(start + idx + 1, arr[idx + 1:])
    func(start, arr[:idx])

func(0, strs)