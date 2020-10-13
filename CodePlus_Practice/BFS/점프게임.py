from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(2)]
check = [[False]*n for _ in range(2)]
q = deque()
q.append((0, 0, 0))
while q:
    col, pos, count = q.popleft()
    if pos+1 > n-1 or pos+k > n-1:
        print(1)
        exit(0)
    if pos+1 > count and arr[col][pos+1] and not check[col][pos+1]:
        check[col][pos+1] = True
        q.append((col, pos+1, count+1))
    if pos-1 > count and arr[col][pos-1] and not check[col][pos-1]:
        check[col][pos-1] = True
        q.append((col, pos-1, count+1))
    if pos+k > count and arr[(col+1) % 2][pos+k] and not check[(col+1) % 2][pos+k]:
        check[(col+1) % 2][pos+k] = True
        q.append(((col+1) % 2, pos+k, count+1))
print(0)