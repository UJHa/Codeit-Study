# 정확성: 100.0
# 합계: 100.0 / 100.0

def get_divisor_count(num):
    result = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result += 1

    result += 1
    return result


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        n = get_divisor_count(i)
        if n % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


# def solution(left, right):
#     answer = 0
#     for i in range(left, right+1):
#         if i ** 0.5 == int(i ** 0.5):
#             answer -= i
#         else:
#             answer += i
#     return answer


s = solution(13, 17)
print(s)