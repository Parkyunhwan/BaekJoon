#  방문 검사를 앞에 하는 것과 뒤에 하는 것의 차이는 무엇인가? -> 앞에서 하면 동시에 들어온 값들이 체크되지 않는다.
#  따라서, 동시에 들어온 중복 값들을 체크하려면 pop후에 방문 체크를 해야한다.

from collections import deque
n, k = map(int, input().split())

q = deque()
check = [False]*100001
q.append((n, 0))
num = 0
while q:

    su, count = q.popleft()
    check[su] = True  #  pop 이후에 체크함으로서 동시에 들어온 것 까지는 인정할 수 있다.
    if su == k:
        print(count)
        num = 1
        while q:
            su, co = q.popleft()
            if co == count:
                if su == k:
                    num += 1
            else:
                break
        print(num)

        exit(0)
    if su - 1 >= 0 and not check[su-1]:
        #check[su - 1] = True # 틀린 코드 ( 맨 첫번째 들어올 때 체크 하기 때문에 )
        #                              동시에 들어온 애들의 갯수를 체크할 수 없다.
        # if su-1 == k:
        #     check[su - 1] = False
        #     num += 1
        # if su-1 == k: #  4 쪽에서 더해서 넘어옴
        #     num += 1
        q.append((su-1, count + 1))
    if su + 1 <= 100000 and not check[su+1]:
        q.append((su+1, count + 1))
    if su*2 <= 100000 and not check[su*2]:
        q.append((su*2, count + 1))


