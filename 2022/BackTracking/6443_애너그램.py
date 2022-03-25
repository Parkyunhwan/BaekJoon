# 그냥 위치로 방문체크를 하면 똑같은 문자여도 탐색을 다시하기 때문에 중복된 문자가 출력된다.
# 이를 방지하기 위해서 문자를 map자료구조에 넣고 갯수를 저장해둔다.
# 같은 문자는 갯수만큼 반복될 수 있다. 하지만 똑같은 깊이에서 두번 나올 순 없다.
def dfs(idx, currWord):
    if idx == len(word):
        print(currWord)
        return

    for ch in worddic:
        if worddic.get(ch) and worddic[ch] > 0:
            worddic[ch] -= 1
            dfs(idx + 1, currWord + ch)
            if not worddic.get(ch):
                worddic[ch] = 1
            else:
                worddic[ch] += 1

N = int(input())
word = []
worddic = {}
for _ in range(N):
    worddic = {}
    word = list(input())
    word.sort()
    for ch in word:
        if not worddic.get(ch):
            worddic[ch] = 1
        else:
            worddic[ch] += 1
    visited = [False] * len(word)
    dfs(0, '')