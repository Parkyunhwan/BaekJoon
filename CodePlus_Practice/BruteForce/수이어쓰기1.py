num = input()
length = len(num)
int_num = int(num)
ten = 10
ten **= (length-1)
diff = (int_num - ten) + 1
answer = diff * length
for i in range(length-1,0,-1):
    answer += i * 9 * (10**(i-1))
print(answer)