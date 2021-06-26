# 폰켓몬(성공)
# 06/24 23:35~00:05
# 정확성: 100.0
# 합계: 100.0 / 100.0
def get_rank(right_number):
    if right_number == 6:
        return 1
    elif right_number == 5:
        return 2
    elif right_number == 4:
        return 3
    elif right_number == 3:
        return 4
    elif right_number == 2:
        return 5
    return 6


def solution(lottos, win_nums):
    max_count, min_count = 0, 0
    for l in lottos:
        if l in win_nums:
            max_count += 1
            min_count += 1
        elif l == 0:
            max_count += 1
    return [get_rank(max_count), get_rank(min_count)]


# s = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
# s = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
s = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
print(s)