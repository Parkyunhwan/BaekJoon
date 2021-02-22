n = int(input())
sang = list(map(int, input().split()))
sang.sort()
m = int(input())
number = list(map(int, input().split()))

for i, val in enumerate(number):
    left = 0
    right = len(sang) - 1
    number[i] = 0
    while left <= right:
        mid = (left + right) // 2
        if sang[mid] < val:
            left = mid + 1
        elif sang[mid] > val:
            right = mid - 1
        else:
            number[i] = 1
            break
for i in number:
    print(i, end=' ')