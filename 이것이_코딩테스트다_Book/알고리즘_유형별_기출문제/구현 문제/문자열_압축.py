# 중간까진 잘 풀었지만
# 다를 때 어떻게 다시 압축문자열을 잡을지 고민했고 for문의 종료 시점을 잡지 못했던 문제
# 파이썬의 리스트의 참조가 넘어가면 그냥 마지막 참조까지만 정상적으로 참조된다.
def solution(s):
    mn = len(s)
    length = len(s)
    for i in range(1, length//2+1):
        comp_str = s[:i]
        count = 1
        tmp = ""
        for j in range(i, length, i):
            tmp_str = s[j:j+i]
            if tmp_str == comp_str:
                count += 1
            else:
                if count >= 2:
                    tmp += str(count) + comp_str
                else:
                    tmp += comp_str
                comp_str = s[j:j+i]
                count = 1
        if count >= 2:
            tmp += str(count) + comp_str
        else:
            tmp += comp_str
        mn = min(mn, len(tmp))
    return mn