# 정확성 100 합 100 성공

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))