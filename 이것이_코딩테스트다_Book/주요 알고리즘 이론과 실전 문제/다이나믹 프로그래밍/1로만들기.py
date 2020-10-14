x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i-1] + 1  # 무조건 증가되는 횟수

    if i % 2 == 0:  # 2의 배수일 때만
        d[i] = min(d[i], d[i // 2] + 1)  # 그전 2의 배수의 최소에 1을 더함
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])





# 틀린 코드 -> 보텀업으로 풀려고 시도했지만  반복문을 통해 어떻게 매번 다른 곱하기를 검사해야 할지 생각하지 못했다.

# while True:
#     if ch[n]:
#         print(ch[n])
#         break
#     count = ch[i]
#     if i * 5 <= n and not ch[i*5]:
#         ch[i*5] = count+1
#     if i * 3 <= n and not ch[i*3]:
#         ch[i*3] = count+1
#     if i * 2 <= n and not ch[i*2]:
#         ch[i*2] = count+1
#     if i - 1 > 1 and not ch[i-1]:
#         ch[i-1] = count+1
