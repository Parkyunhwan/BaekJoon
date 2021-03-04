'''
1. 풀이 생각 하기
짝수 x 짝수 의 경우를 제외하면 모든 칸을 방문할 수 있다. (모든 칸을 방문하는 경로가 최댓 값)
그런데 짝수 x 짝수는 최댓값이 될 수 있는 경우의 수가 여러가지 이다.

이 경우들을 어떻게 구할 수 있을까?
--- 못품
1. R이 홀수 일 때 ex) 3x2 .. 3x3
2. C가 홀수 일 때
=> 모든 칸을 방문 가능

3. 짝수 x 짝수
    1. 체스판에서 흰칸에서 흰칸으로 가려면 짝수번 이동해야만 한다.
        but, 모든 칸을 방문하려면 홀수 * 짝수 + 홀수 = 홀수번 이동
    2. 한 칸을 버려야 하는데 이 때도 검은색을 버려야 한다.
    가장 적은 기쁨칸을 선택한다.

'''
r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]
result = []
if r % 2:
    for i in range(r):
        if i % 2 == 0: # even
            result.append('R' * (c - 1))
        else:
            result.append('L' * (c - 1))
        if i != r - 1:
            result.append('D')
elif c % 2:
    for i in range(c):
        if i % 2 == 0:
            result.append('D' * (r - 1))
        else:
            result.append('U' * (r - 1))
        if i != c - 1:
            result.append('R')
else:
    min_x, min_y = 0, 1  # 다음 방향 지정
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1 and arr[min_x][min_y] > arr[i][j]:  # 홀수가 검은 칸!
                min_x, min_y = i, j

    x1, y1 = 0, 0
    x2, y2 = r - 1, c - 1
    result2 = []
    while x2 - x1 > 1:
        if x1 / 2 < min_x / 2: # 1 이상 차이나려면 2줄 차이가 나야함
            print("aaaa")
            result.append('R' * (c - 1))
            result.append('D')
            result.append('L' * (c - 1))
            result.append('D')
            x1 += 2  # 두 줄 아래로 갔으므로
        if min_x / 2 < x2 / 2: # 똑같이 2줄 이상 차이가 나야 1 이상 차이가남
            result2.append('R' * (c - 1))
            result2.append('D')
            result2.append('L' * (c - 1))
            result2.append('D')
            x2 -= 2

    while y2 - y1 > 1:
        if y1 / 2 < min_y / 2:
            result.append('D')
            result.append('R')
            result.append('U')
            result.append('R')
            y1 += 2
        if min_y / 2 < y2 / 2:
            result2.append('D')
            result2.append('R')
            result2.append('U')
            result2.append('R')
            y2 -= 2

    if min_y == y1:
        result.append('R')
        result.append('D')
    else:
        result.append('D')
        result.append('R')
    result2 = ''.join(result2)
    result2 = ''.join(list(reversed(result2)))
    result = ''.join(result)
    print(result)
    print(result2)
    result += result2
    exit(0)
print(''.join(result))