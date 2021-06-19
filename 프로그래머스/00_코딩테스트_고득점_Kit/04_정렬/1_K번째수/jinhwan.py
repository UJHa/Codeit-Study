# K번째수(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        cut_list = sorted(array[i-1:j])
        answer.append(cut_list[k - 1])

    return answer


s = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])  # [5, 6, 3]
print(s)