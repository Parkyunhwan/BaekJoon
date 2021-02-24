import sys
n, m = map(int, sys.stdin.readline().split())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))


def merge(li1, li2):
    result = []
    len1 = len(li1)
    len2 = len(li2)

    while len1 > 0 or len2 > 0:
        len1 = len(li1)
        len2 = len(li2)
        if len1 > 0 and len2 > 0:
            if li1[0] <= li2[0]:
                result.append(li1[0])
                li1.pop(0)
            else:
                result.append(li2[0])
                li2.pop(0)
        elif len1 > 0:
            result.append(li1[0])
            li1.pop(0)
        elif len2 > 0:
            result.append(li2[0])
            li2.pop(0)
    return result


arr = merge(arrA, arrB)

for v in arr:
    print(v, end=' ')
