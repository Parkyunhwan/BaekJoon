n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

repetition = m // (k+1)
remainder = m % (k+1)
sm = repetition*(arr[0]*k + arr[1]) + remainder*arr[0]
print(sm)