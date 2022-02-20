import math

N = int(input())
arr = [False] * 1000001
arr[0] = True

def findPrime():
    for i in (2, int(math.sqrt(1000001)) + 1):
        if arr[i]:
            continue
        for j in (1, i + 1):
            currNum = i * j
            if (currNum > 100000):
                break
            if not arr[currNum]:
                arr[currNum] = True


def findAnswer(start):
    for num in (start, 1000001):
        if not arr[num]:
            mid = len(str(num)) // 2
            front, end = 0, 0
            if mid % 2 == 0: # even
                front = arr[:mid]
                end = arr[mid:]
            else:
                front = arr[:mid]
                end = arr[mid + 1:]
        if end == front:
            print(num)
            break



findPrime()
findAnswer(N)




