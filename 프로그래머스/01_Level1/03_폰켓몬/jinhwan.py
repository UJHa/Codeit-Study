# 폰켓몬(실패)
# 06/24 09:10~
# 정확성: 30.0
# 합계: 30.0 / 100.0
from itertools import combinations


def solution(nums):
    answer = 0
    for i in combinations(nums, len(nums) // 2):
        answer = max(answer, len(set(i)))
    return answer


# s = solution([3, 1, 2, 3]) == 2
# s = solution([3, 3, 3, 2, 2, 4]) == 3
s = solution([3, 3, 3, 2, 2, 2]) == 2
print(s)
