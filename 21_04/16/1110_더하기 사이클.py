n = int(input())
save = n
count = 1
while True:
    ten = n // 10
    remain = n % 10

    sum_num = ten + remain

    n = remain * 10
    n += (sum_num % 10)
    if save == n:
        print(count)
        break
    count += 1