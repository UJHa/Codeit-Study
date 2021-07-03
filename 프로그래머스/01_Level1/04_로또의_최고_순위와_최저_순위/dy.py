def solution(lottos, win_nums):
    answer = []
    rank, zero = 7, 0

    for num in lottos:
        if num in win_nums:
            rank -= 1
        elif num == 0:
            zero += 1
    answer.append(min(rank - zero, 6))
    answer.append(min(rank, 6))
    return answer
