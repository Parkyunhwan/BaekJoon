inputNum = int(input())
nc = [0] * (inputNum+1)
for i in range(1, inputNum+1):
    nc[i] = i for j in range(1, i):
        if (j * j) > i:
            break
        nc[i] = min(nc[i], nc[i - j * j] + 1)
print(nc[inputNum])
