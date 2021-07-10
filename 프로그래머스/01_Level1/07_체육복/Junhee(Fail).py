# 정확성: 91.7 합계: 91.7 / 100.0 FAIL

def solution(n, lost, reserve):
    answer = n - len(lost)  # 잃어버리지 않은 사람 수 
    
    for r in reserve:
        # 여벌은 있는데 잃어버림 
        if r in lost:  
            answer += 1
            lost[lost.index(r)] = 999  # 나 자신 제외 
        
        # 여벌도 있고 잃어버리지도 않음 
        elif r not in lost:  
            for i, l in enumerate(lost):
                if l == r-1 or l == r+1:  # 빌려줄 수 있는 경우
                    lost[i] = 999  # 빌려준 학생 제외 
                    answer += 1
                    break
    
    return answer