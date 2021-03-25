import sys
n, k = map(int, input().split())

if k < 5:
    print(0)
    exit(0)

k -= 5
alpha = [False] * 26
alpha[ord('a') - ord('a')] = True
alpha[ord('n') - ord('a')] = True
alpha[ord('t') - ord('a')] = True
alpha[ord('i') - ord('a')] = True
alpha[ord('c') - ord('a')] = True
mx = 0
arr = []
set_sub = {'a', 'n', 't', 'i', 'c'}

for _ in range(n):
    arr.append(set(sys.stdin.readline().rstrip()[4:-4]))

set_arr = set()
for a in arr:
    set_arr = set_arr.union(a)

set_arr = set_arr.difference(set_sub)
set_arr = list(set_arr)

def check_word():
    global mx
    count = 0
    for a in arr:
        check = True
        for val in a:
            if not alpha[ord(val) - ord('a')]:
                check = False
                break
        if check:
            count += 1
    mx = max(mx, count)


def select_alpha(start, index):
    if index == k or index == len(set_arr):
        check_word()
        return

    for t in range(start, len(set_arr)):
        i = ord(set_arr[t]) - ord('a')
        if not alpha[i]:
            alpha[i] = True
            select_alpha(t, index + 1)
            alpha[i] = False

select_alpha(0, 0)
print(mx)