def solution(board, moves):
    answer = 0

    vertical_list = [[] for _ in board]
    for i, b in enumerate(board):
        for j, doll in enumerate(b):
            if doll != 0:
                vertical_list[j].append(doll)

    for v in vertical_list:
        print(v)

    basket = []
    for m in moves:
        if len(vertical_list[m-1]) == 0:
            continue
        print(m-1, vertical_list[m-1])

        doll_index = vertical_list[m-1].pop(0)
        if len(basket) == 0:
            basket.append(doll_index)
        else:
            if basket[-1] == doll_index:
                del basket[-1]
                answer += 2
            else:
                basket.append(doll_index)
        print(basket)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))