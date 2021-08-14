def solution(s):
    answer = 0
    cor = {'(':')', '{':'}', '[':']'}
    
    for i in range(len(s)): # x(0 ≤ x < (s의 길이)) 만큼 반복
        new = list(s[i:] + s[:i]) # 회전한 리스트
        check = [] # 빈 리스트
        
        while new:
            temp = new.pop(0)
            if not check:
                check.append(temp) # temp 추가
            else:
                if check[-1] in cor.values(): # 닫힌 쪽이면 break
                    break
                if cor[check[-1]] == temp: # 닫힌 쪽 아니고, temp와 동일하면 제거
                    check.pop()
                else: # 닫힌 쪽 아니고, temp와 다르면 추가
                    check.append(temp)
                    
        if not check: # 다 지운 경우 최종 answer +1
            answer += 1
    
    return answer
