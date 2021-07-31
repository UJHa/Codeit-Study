# 정확성: 60.2
# 효율성: 39.8
# 소요시간: 20분

def solution(s):
    
    lst = []
    
    for s_value in s:
        if not lst:
            lst.append(s_value)
        elif s_value == lst[-1]:
            lst.pop()
        else:
            lst.append(s_value)       
        
    if len(lst) == 0:  # 모두 제거가 되었다면 
        return 1  # 1
    else:
        return 0
