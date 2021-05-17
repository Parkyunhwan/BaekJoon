mx = 0


def solution(numbers, target):
    def dfs(idx, curr, value, length, numbers, target):
        global mx
        if idx == length:
            if target == value:
                mx += 1
            return

        dfs(idx + 1, curr + 1, value + numbers[curr], length, numbers, target)
        dfs(idx + 1, curr + 1, value - numbers[curr], length, numbers, target)

    dfs(0, 0, 0, len(numbers), numbers, target)
    return mx