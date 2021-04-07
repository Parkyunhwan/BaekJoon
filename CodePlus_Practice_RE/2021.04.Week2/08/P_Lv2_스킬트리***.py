'''
    쉬워보이는데 어려운 문제 ...다시

'''
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        list = []
        flag = True

        for j in range(len(skill_tree)):
            if skill_tree[j] in skill:
                list.append(skill_tree[j])

        for k in range(len(list)):
            if list[k] != skill[k]:
                flag = False
                break

        if flag:
            answer += 1

    return answer