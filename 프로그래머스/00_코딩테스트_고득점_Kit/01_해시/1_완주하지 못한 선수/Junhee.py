# 100% 통과

def solution(participant, completion):
    # runner 딕셔너리에 참가자 목록 추가
    # Key는 이름, Value는 명수
    runner = {}
    # 목록 만들기
    for name in participant:
        runner[name] = 0
    # 중복 고려하여 명수 추가
    for name in participant:
        runner[name] += 1
    
    # 완주하지 못한 선수의 이름 출력 
    answer = ''
    for name in completion:
        if name in runner:
            runner[name] -= 1
    
    for i in runner.items():
        if i[1] == 1:
            answer = i[0]
            break
            
    return answer