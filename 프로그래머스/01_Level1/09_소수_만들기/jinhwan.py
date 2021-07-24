# 소수 만들기
# 정확성: 100.0
# 합계: 100.0 / 100.0
from itertools import combinations


def is_prime(pnum, plist):
    if plist.get(pnum) is not None:
        return plist[pnum]

    can_divide = False
    for i in range(2, pnum // 2):
        if pnum % i == 0:
            can_divide = True
    plist[pnum] = not can_divide

    return plist[pnum]


def solution(nums):
    answer = 0
    # 0, 1의 경우 False로 저장
    prime_dict = {}
    # if is_prime(test_num, prime_list):
    for tu in combinations(nums, 3):
        if is_prime(sum(tu), prime_dict) is True:
            answer += 1
        # print(tu, sum(tu), is_prime(sum(tu), prime_dict))
    return answer


s= solution([1,2,3,4])