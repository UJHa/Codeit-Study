# 정확성: 100.0 합계: 100.0 / 100.0

def solution(n, lost, reserve):
    wear = [1] * n  # 전체 학생 줄 세우기
    
    # 학생들 체육복 잔여 체크
    for l in lost:
        wear[l-1] -= 1  # 도난당한 학생들
    for r in reserve:
        wear[r-1] += 1  # 여분있는 학생들
    
    # 빌려주기
    for i, w in enumerate(wear):
        if w == 2:  # 여분이 있으면 빌려준다 
            if i-1 >= 0 and wear[i-1] == 0:
                wear[i] -= 1
                wear[i-1] += 1
            elif i+1 <= n-1 and wear[i+1] == 0:
                wear[i] -= 1
                wear[i+1] += 1
                
    return n-(wear.count(0))