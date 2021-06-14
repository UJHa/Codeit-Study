# H-Index(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(citations):
    answer = 0
    for index in range(len(citations)):
        up_count = 0
        down_count = 0
        for c in range(citations):
            if index <= c:
                up_count += 1
            if index >= c:
                down_count += 1

        if down_count <= index <= up_count:
            answer = index
        index += 1
    return answer


# s = solution([3, 0, 6, 1, 5])  # 3
# s = solution([7, 2, 9, 8, 5])  # 7
s = solution([22, 42])  # 3
print(s)
