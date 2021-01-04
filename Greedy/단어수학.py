n = int(input())

arr = [input() for _ in range(n)]
alpha = [0] * 26
for w in arr:
    for i in range(len(w)):
        alpha[ord(w[i]) - ord('A')] += pow(10, len(w) - i - 1)  # 각 알파벳의 값을 자릿수에 맞춰 적용시

alpha.sort(reverse=True)
result = 0
num = 9
for al in alpha:
    result += (al * num)  # 가장 큰 알파벳부터 가장 큰 숫자를 적용해 총 합을 구한다.
    num -= 1
print(result)