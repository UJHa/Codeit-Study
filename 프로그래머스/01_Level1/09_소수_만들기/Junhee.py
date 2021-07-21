from itertools import combinations as cb

def solution(nums):
    """입력받은 정수 배열에서 세 정수의 조합 중 소수의 개수 구하기
    
    Args: 
        nums: 범위 1~1,000 && 개수 3~50인 중복 없는 정수 list 

    Returns:
        answer: 소수가 되는 조합의 개수 
    """
    answer = 0

    for a, b, c in cb(nums, 3):
        if is_prime(a+b+c) == True:
            answer += 1

    return answer


def is_prime(num):
    """소수인지 아닌지 판별하는 함수
    루트를 이용해 약수의 중간값을 범위로 검증

    Args:
        num: 검증할 6 이상의 정수

    Returns:
        True: 소수
        False: 소수가 아님
    """
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

