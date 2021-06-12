# 가장 큰 수(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(numbers):
    l = []
    max_length = 4
    for number in numbers:
        origin_num = str(number)
        # 정렬을 위해 4자리의 숫자로 변환
        key_num = origin_num * max_length
        key_num = int(key_num[:max_length])

        l.append([key_num, origin_num])

    l = sorted(l, reverse=True)
    return str(int("".join([item[1] for item in l])))


# s = solution([6, 10, 2])  # "6210"
s = solution([3, 30, 34, 5, 9])  # "9534330"
print(s)
