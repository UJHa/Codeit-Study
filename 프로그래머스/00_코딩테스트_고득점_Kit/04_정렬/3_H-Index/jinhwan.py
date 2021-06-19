# H-Index(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(citations):
    sort_list = sorted(citations)
    _length = len(sort_list)
    for index in range(_length):
        if citations[index] >= _length - index:
            return _length - index
    return 0


s = solution([3, 0, 6, 1, 5])  # 3
# s = solution([7, 2, 9, 8, 5])  # 7
# s = solution([22, 42])  # 3
print(s)
