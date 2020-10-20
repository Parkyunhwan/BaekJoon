# 1회차 -> 런타임에러
# 1. 소팅을 어떻게 해야 할지가 중요한 요소였다
# 2. 분모가 0일때 예외처리를 해주었는가도 굉장히 중요했다.
# count()로 숫자의 갯수를 세면 상당한 시간이 걸려서 못깰줄 알았는데 모범답안은 그렇게 되어있었다.
def solution(N, stages):
    stages.sort()
    answer = []
    length = len(stages)
    fail = []
    k = 0
    for i in range(1, N + 1):
        count = 0
        for j in range(k, len(stages)):
            k = j
            if stages[j] == i:
                count += 1
            else:
                break
        if length == 0:
            f = 0
        else:
            f = count / length
        # 실패 코드 length 0에 대한 예외처리가 없었다.
        # fail.append((i, count/length)) ==> 나눗셈 시 분모 0 예외처리는 런타임 에러를 피하기 위해 필수이다.
        fail.append((i, f))
        length = length - count

    # fail.sort(reverse=True, key=lambda x:x[1])
    fail.sort(key=lambda x: (-x[1]))
    for f in fail:
        answer.append(f[0])
    return answer