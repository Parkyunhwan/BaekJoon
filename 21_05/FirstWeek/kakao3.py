def solution(n, k, cmd):
    answer = ['O'] * n

    del_stack = []
    arr = [i for i in range(n)]
    curr = k
    for curr_cmd in cmd:
        curr_cmd = curr_cmd.split()
        cmd_length = len(curr_cmd)
        if curr_cmd[0] == 'D':
            curr += int(curr_cmd[1])
        elif curr_cmd[0] == 'U':
            curr -= int(curr_cmd[1])
        elif curr_cmd[0] == 'C':
            if len(arr) - 1 == curr:
                del_stack.append(arr[-1])
                del arr[-1]
            else:
                del_stack.append(arr[curr])
                del arr[curr]
        elif curr_cmd[0] == 'Z':
            pos = del_stack.pop()
            arr.insert(pos, pos)

    print(arr)
    print(del_stack)
    for val in del_stack:
        answer[val] = 'X'
    print(answer)
    return ''.join(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])