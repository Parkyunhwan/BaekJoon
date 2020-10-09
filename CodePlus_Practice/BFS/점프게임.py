from collections import deque
n, k = map(int, input().split())
left = list(map(int, list(input())))
right = list(map(int, list(input())))
q = deque()
q.append((0, 0, -1))
while q:
    pos, dir, count = q.popleft()
    if pos >= n:
        print(1)
        exit(0)

    if dir == 0:
        line = left
    else:
        line = right
    for k in range(3):
       # if pos - 1 > count and pos + 1 < n:
            if k == 0: # +1
                if pos + 1 >= n:
                    print("k")
                    print(1)
                    exit(0)
                if line[pos + 1] == 1:
                    print("a" + str(line[pos+1]))
                    q.append((pos+1, dir, count+1))
            elif k == 1: # -1
                if pos - 1 <= count:
                    continue
                if line[pos - 1] == 1:
                    print("a" + str(line[pos-1]))
                    q.append((pos-1, dir, count+1))
            else:
                if line is left:
                    line = right
                else:
                    line = left
                if pos + k >= n:

                    print(1)
                    exit(0)
                else:
                    if line[pos+k] == 1:
                        print("a" + str(line[pos + k]))
                        q.append((pos+k, dir+1%2, count+1))
print(0)