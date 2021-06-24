# 폰켓몬(성공)
# 06/24 09:10~09:35
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(nums):
    answer = 0
    pick_count = len(nums) // 2
    temp = set(nums)
    if len(temp) < pick_count:
        answer = len(temp)
    else:
        answer = pick_count

    return answer


# s = solution([3, 1, 2, 3]) == 2
# s = solution([3, 3, 3, 2, 2, 4]) == 3
s = solution([3, 3, 3, 2, 2, 2]) == 2
print(s)
