def solution(n, k):
    answer = 0
    visited = [False] * (k + 1)

    val1 = n % k
    val2 = int(str(n) * 2) % k
    diff = val2 - val1

    val = n % k
    count = 1
    while True:
        if val == 0:
            return count
        if visited[val]:
            return -1
        visited[val] = True
        val = (val + diff) % k
        count += 1
    return answer