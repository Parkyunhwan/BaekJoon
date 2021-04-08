import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
import sys


def dfs(idx, plan, price, sum_value):
    global min_value
    if idx == 12:
        min_value = min(min_value, sum_value)
        return
    dfs(idx + 1, plan, price, sum_value + (plan[idx + 1] * price[0]))
    dfs(idx + 1, plan, price, sum_value + price[1])
    if idx <= 9:
        dfs(idx + 3, plan, price, sum_value + price[2])


T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    min_value = sys.maxsize
    # ///////////////////////////////////////////////////////////////////////////////////
    # day_price, month_price, month3_price, year_price
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    dfs(0, plan, price, 0)
    min_value = min(min_value, price[3])
    print("#{} {}".format(test_case, min_value))

