def solution(s):
    answer = 0
    cor = {'(':')', '{':'}', '[':']'}
    
    for i in range(len(s)): # x(0 ≤ x < (s의 길이)) 만큼 반복
        right = list(s[i:] + s[:i]) # 회전한 리스트
        left = [] # 빈 리스트
        
        while right:
            temp = right.pop(0)
            if not left:
                left.append(temp) # temp 추가
            else:
                if left[-1] in cor.values(): # 닫힌 쪽이면 break
                    break
                if cor[left[-1]] == temp: # 닫힌 쪽 아니고, temp와 동일하면 제거
                    left.pop()
                else: # 닫힌 쪽 아니고, temp와 다르면 추가
                    left.append(temp)
                    
        if not left: # 다 지운 경우 최종 answer +1
            answer += 1
    
    return answer
