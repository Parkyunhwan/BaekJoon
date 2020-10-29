# words	queries	result
# words ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# quries ["fro??", "????o", "fr???", "fro???", "pro?"]
# result [3, 2, 4, 1, 0]

# 1. 접두어 와 접미어 두가지 종류가 있다.
# 2. 단어는 단어 길이로 나눌 수 분류할 수 있다.
# words	queries	result
# words ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# quries ["fro??", "????o", "fr???", "fro???", "pro?"]
# result [3, 2, 4, 1, 0]

# 1. 접두어 와 접미어 두가지 종류가 있다.
# 2. 단어는 단어 길이로 나눌 수 분류할 수 있다.
import bisect


def count_by_range(array, left, right):
    left_value = bisect.bisect_left(array, left)
    right_value = bisect.bisect_right(array, right)
    return right_value - left_value


def solution(words, queries):
    answer = []
    arr = dict()
    reverse_arr = dict()
    for word in words:
        length = len(word)
        if not arr.get(length):
            arr[length] = [word]
            reverse_arr[length] = [word[::-1]]
        else:
            arr[length].append(word)
            reverse_arr[length].append(word[::-1])
    for k in arr.keys():
        arr[k].sort()
        reverse_arr[k].sort()
    for query in queries:
        if not len(query) in arr:
            res = 0
        elif query[0] != '?':
            res = count_by_range(arr[len(query)], query.replace('?', 'a'), query.replace('?','z'))
        else:
            res = count_by_range(reverse_arr[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?', 'z'))
        answer.append(res)
    return answer