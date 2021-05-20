def bubble_sort(arr):
    count = 0
    print("count %d" % count)
    for a in arr:
        print(a, end=' ')
    print()
    print()
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
                print("count %d" % count)
                for a in arr:
                    print(a, end=' ')
                print()
                print()

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    bubble_sort(arr)