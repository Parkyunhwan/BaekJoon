import sys
n, k = map(int, input().split())
arr = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]
alpha = [False] * 26
arr_set = set()
if k < 5:
    print(0)
    exit(0)
else:
    k -= 5
al = ['a', 'n', 't', 'i', 'c']
for a in al:
    alpha[ord(a)-ord('a')] = True
mx = -1

for word in arr:
    arr_set = arr_set.union(set(list(word)))

print(list(arr_set))


def solve(start, index):
    global mx
    if index == k:
        count = 0
        for ar in arr:
            flag = True
            for a in ar:
                if not alpha[ord(a)-ord('a')]:
                    flag = False
                    break
            if flag:
                count += 1
        mx = max(mx, count)
        return
    else:
        for val in list(arr_set):
            i = ord(val) - ord('a')
            if not alpha[i]:
                alpha[i] = True
                solve(i, index+1)
                alpha[i] = False
        return


solve(0, 0)

print(mx)