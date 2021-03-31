def solution(board, moves):
    answer = 0
    length = len(board)

    box = []
    for row in board:
        print(row)
    print()
    for move in moves:
        move = move - 1
        for i in range(length):
            if board[i][move] != 0:
                box.append(board[i][move])
                board[i][move] = 0
                break

        if len(box) > 1:
            if box[-2] == box[-1]:
                answer += 2
                box.pop()
                box.pop()

    return answer