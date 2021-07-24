# 예상 대진표
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n,a,b):
    answer = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer


s = solution(8, 4, 7)
print(s)