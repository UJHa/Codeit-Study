# 진행중 

def solution(genres, plays):
    # 장르의 수록 순서를 결정
    gen = {}
    for i in genre:
        gen[i] = 0
    for i, j in zip(genres, plays):
        gen[i] += j
    
    
    
    answer = []
    return answer