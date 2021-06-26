
def solution(a_lst, b_lst):
    
    answer = 0
    
    for a, b in zip(a_lst, b_lst):
        answer += a*b
        
    return answer
