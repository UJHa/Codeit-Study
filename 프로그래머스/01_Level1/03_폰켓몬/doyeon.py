def solution(nums):
    p = len(nums)/2
    numsSet = list(set(nums))
    if (len(numsSet) <= p):
        return len(numsSet)
    else:
        return p
