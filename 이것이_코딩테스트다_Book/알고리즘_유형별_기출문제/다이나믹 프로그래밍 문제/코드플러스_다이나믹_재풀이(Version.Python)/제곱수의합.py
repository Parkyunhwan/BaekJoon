# inputNum = int(input())
# nc = [0] * (inputNum+1)
# for i in range(1, inputNum+1):
#     nc[i] = i
#     for j in range(1, i):
#         if (j * j) > i:
#             break
#         nc[i] = min(nc[i], nc[i - j * j] + 1)
# print(nc[inputNum])
if __name__ == '__main__':
    n = int(input())
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = i
        for j in range(1, n + 1):
            if j * j > i:
                break
            d[i] = min(d[i], d[i - (j * j)] + 1)
    print(d[n])
