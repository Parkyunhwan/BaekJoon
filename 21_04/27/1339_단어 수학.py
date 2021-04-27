from collections import defaultdict
N = int(input())

words = []
for i in range(N):
    words.append(input())


char_num = defaultdict(int)

for word in words:
    for j in range(len(word)):
        char = word[len(word) - j - 1]
        char_num[char] += (10 ** j)

# print(char_num)
# print(char_num.items())
# print(char_num.keys())

num_sort = sorted(char_num.items(),key= lambda x: x[1], reverse=True)
sm = 0
max_val = 9
for value in num_sort:
    sm += (value[1] * max_val)
    max_val -= 1
print(sm)