'''
    최댓값이 출력되려면 마지막에 'A'를 입력하거나 ctrl + v를 눌러야한다.
    따라서, 나머지 두 개를 누른 경우는 최댓값이 될 수 없다.

    n보다 작은 수부터 천천히 최댓값을 구해나가보자.

    기본적으로 1 ~ 6까지 최댓값은 각자 인덱스값이다.

    그리고 7부터 최댓값을 구하면된다.
    최댓값은 n - 1의 최댓값에서 + 1을 하거나
    n - 3 부터 열심히 작업해 ctrl+A, ctrl+c, ctrl+v를 눌러 n - 3의 최댓값에 *2를 할 수 있다.

    더 생각해보면

    n - 4 부터 열심히 작업하면 ctrl+A, ctrl+c, ctrl+v, ctrl+v 붙여넣기 두번을 할 수 있으므로
    n - 4의 최댓값에 *3을 한 것과 같다.
    .
    .
    n - n이 될 때까지 진행해서 최댓값을 계산해준다.

    여기서 +1 해주는 것은 7이상부터는 최댓값이 나올 수 없으므로 제외시켜줘도 된다.
'''
# dp 풀이
n = int(input())

dp = [0] * (n + 1)

if n <= 6:
    print(n)
    exit(0)

for i in range(1, 7):
    dp[i] = i

for i in range(7, n + 1):
    for j in range(3, n + 1):
        dp[i] = max((j - 1) * dp[i - j], dp[i])

print(dp[n])



# 시간초과
'''
from collections import deque
from collections import defaultdict
n = int(input())

q = deque()
q.append((0, 0, 0, 0))
dic = defaultdict(int)

result = 0
while q:
    text, buf, select, count = q.popleft()
    if count > n:
        break
    result = max(result, text)
    val = str(text) + str(buf) + str(select)
    if dic[val] > 0:
        continue
    dic[val] += 1
    q.append((text + 1, buf, 0, count + 1))
    q.append((text, buf, text, count + 1))
    q.append((text, select, 0, count + 1))
    q.append((text + buf, buf, 0, count + 1))


print(result)
'''