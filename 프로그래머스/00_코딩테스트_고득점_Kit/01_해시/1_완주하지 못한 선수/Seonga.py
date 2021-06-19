# 완주하지 못한 선수
# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0

# 완주하지 못한 선수
def solution(participant, completion):
    
    answer = ''
    
    bucket = 0
    dict_ = {}  # 마라톤에 참여한 선수들의 이름을 담을 딕셔너리
    
    for m in participant:
        dict_[hash(m)] = m  # 마라톤 참여 선수의 해시값을 key, 마라톤 참여 선수 이름을 value
        bucket += int(hash(m))  # 마라톤에 참여한 선수들의 해시값을 계속 더함 
        
    for n in completion:
        bucket -= int(hash(n))  # 마라톤에 참여한 선수들의 해시값을 뺌
    
    answer = dict_[bucket]  # 마라톤에 참여하지 않은 선수들의 해시값에 해당하는 value
    
    return answer
