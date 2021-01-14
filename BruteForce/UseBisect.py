from bisect import bisect_left, bisect_right

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

'''
결과값
5 (5의 바로 앞 인덱스)
6 (5의 바로 뒤 인덱스)
'''
