n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
    arr[i][1] = int(arr[i][1])
arr = sorted(arr, key=lambda com: com[1])  #  lambda (함수 인자) : (함수 리턴)
print(arr)
arr.reverse()
for a in arr:
    print(a[0], end=" ")