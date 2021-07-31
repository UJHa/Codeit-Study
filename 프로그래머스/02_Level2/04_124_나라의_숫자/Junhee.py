# 정확성: 70.0 효율성: 30.0 합계: 100.0 / 100.0

def solution(n):
    answer = ''
    
    while n:
        num = n % 3
        
        if num == 1: 
            answer += '1'
            n //= 3
        elif num == 2:
            answer += '2'
            n //= 3
        elif num == 0:
            answer += '4'
            n = n // 3 - 1
        
    return answer[::-1]