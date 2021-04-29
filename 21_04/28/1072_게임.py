X, Y = map(int, input().split())

init_Z = (100  * Y) // X

if init_Z >= 99:
    print(-1)
    exit(0)

low = 0
high = int(1e9)

min_count = int(1e9)
while low <= high:
    mid = (low + high) // 2
    Z = (100 * (Y + mid)) // (X + mid)
    if Z <= init_Z:
        low = mid + 1
        min_count = mid + 1
    else:
        high = mid - 1

print(min_count)
