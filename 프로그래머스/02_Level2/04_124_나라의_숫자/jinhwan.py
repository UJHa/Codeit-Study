# 124 나라의 숫자(성공)
# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0

def solution(n):
    answer = ''
    change_dict = {1: '1', 2: '2', 0: '4'}

    while n != 0:
        next_num = n % 3
        answer = change_dict[next_num] + answer
        if n % 3 == 0:
            n -= 3
        else:
            n -= next_num
        n //= 3
    return answer


s = solution(1) == '1'
# s = solution(2) == '2'
# s = solution(3) == '4'
# s = solution(4) == '11'
# s = solution(10) == '41'
print(s)