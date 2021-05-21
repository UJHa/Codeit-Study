# 완주하지 못한 선수
# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0

def solution(participant, completion):
    answer = ''
    
    bucket = 0
    dict_ = {}
    
    for m in participant:
        dict_[hash(m)] = m
        bucket += int(hash(m))
        
    for n in completion:
        bucket -= int(hash(n))
    
    answer = dict_[bucket]
    
    return answer
