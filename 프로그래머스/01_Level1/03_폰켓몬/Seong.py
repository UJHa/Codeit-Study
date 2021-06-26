
def solution(number_lst):
    
    answer = 0
    length = len(number_lst)/2
    
    num_unique = list(set(number_lst))
    
    if len(num_unique) > length:
        answer = length
        
    else:
        answer = len(num_unique) 
        
    return answer
