
def solution(absolutes, signs):
        
    answer = 0
    
    for i, num in enumerate(absolutes):
        if signs[i]:    
            sign_label = 1
        else:
            sign_label = -1
        
        answer += num * sign_label
            
    return answer
