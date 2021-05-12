from itertools import combinations


def sum_numbers(numbers, indexs):
    result = 0
    for i, num in enumerate(numbers):
        add_num = num
        if i in indexs:
            add_num = (-add_num)
        result += add_num
    return result


def solution(numbers, target):
    answer = 0
    temp = [i for i in range(len(numbers))]
    # print(temp)
    for i in range(1, len(numbers)+1):
        for tu in combinations(temp, i):
            if target == sum_numbers(numbers, tu):
                answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 4))