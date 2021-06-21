arr = [[0] * 15 for _ in range(5)]

for i in range(5):
    words = input()
    for j in range(len(words)):
        arr[i][j] = words[j]

result = []
for j in range(15):
    count = 0
    for i in range(5):
        if arr[i][j] != 0:
            result.append(arr[i][j])
        else:
            count += 1
    if count == 5:
        break

print(''.join(result))
