N, B = input().split()

B = int(B)
result = 0
pi = 0

for i in range(len(N) - 1, -1, -1):
    char = N[i]
    if char.isalpha():
        number = ord(char) - ord('A') + 10
    else:
        number = int(char)
    result += (number * pow(B, pi))
    pi += 1
print(result)
