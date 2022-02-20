import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))



def solve():
    sumValue = 0
    minLength = sys.maxsize
    left, right = 0, 0
    while left < N:
        if sumValue < S:
            if right == N:
                break
            sumValue += arr[right]
            print(f'sumValue {sumValue} , arr[right] {arr[right]}')
            right += 1

        elif sumValue >= S:
            legnth = right - left
            minLength = min(minLength, legnth)
            sumValue -= arr[left]
            left += 1

    return minLength

result = solve()
if result != sys.maxsize:
    print(result)
else:
    print(0)
