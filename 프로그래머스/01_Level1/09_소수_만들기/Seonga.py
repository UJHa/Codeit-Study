from itertools import combinations

def price_number_check(sum_value):
    i = 2
    while i < sum_value:
        if sum_value % i == 0:  # 다른 숫자로 나누어떨어지면 
            return False  # 소수가 아님
            break
        i += 1
    return True

    
def solution(nums):
   
    answer = 0
    nums_comb_lst = list(combinations(nums,3))

    for v in nums_comb_lst:
        
        sum_value = sum(v)
        print(sum_value)
        
        if price_number_check(sum_value) == True:
            answer += 1
            
    return answer
