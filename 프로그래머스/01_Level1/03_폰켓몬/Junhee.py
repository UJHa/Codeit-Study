# 정확성 100 합 100 성공

def solution(nums):
    answer = 0
    n = len(nums) // 2
    s = len(set(nums))
    return min(n, s)