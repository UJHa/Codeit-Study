def solution(answers):
    cnt = [0,0,0]
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10
        
        if p1[a1] == answers[i]:
            cnt[0] += 1
        if p2[a2] == answers[i]:
            cnt[1] += 1
        if p3[a3] == answers[i]:
            cnt[2] += 1
            
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
        
    return answer
