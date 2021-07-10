# 정확성: 53.8 합계: 53.8 / 100.0 FAIL

def solution(str1, str2):
    _str1 = make_multiset(str1)
    _str2 = make_multiset(str2)

    return make_jaccard(_str1, _str2)
    

# 다중집합 만들기 
def make_multiset(str0):
    _str = []
    str0 = str0.lower()
    
    for i in range(len(str0)-1):
        if 'a' <= str0[i] <= 'z' and 'a' <= str0[i+1] <= 'z':
            _str.append(str0[i]+str0[i+1])

    return _str


# 자카드 유사도 구하기 
def make_jaccard(_str1, _str2):
    # 둘 다 공집합일 경우
    if not _str1 and not _str2:
        return 65536
    
    sum_union = 0
    sum_inter = 0
    list_str = list(set(_str1) | set(_str2))
    
    for s in list_str:
        if s in _str1 or s in _str2:
            sum_union += 1
        if s in _str1 and s in _str2:
            sum_inter += 1
        
    return int((sum_inter/sum_union)*65536)
