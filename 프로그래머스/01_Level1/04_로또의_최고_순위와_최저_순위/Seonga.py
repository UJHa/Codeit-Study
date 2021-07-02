# 당첨된 로또 번호의 개수 = 최저순위
# 로또 번호에서 알아볼 수 없는 숫자인 0의 개수 + 당첨된 로또 번호의 개수 = 최고순위

def solution(lottos, win_nums):
    
    rank_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    i = 0  
    
    count_zero = lottos.count(0)
    
    for lotto_value in lottos:
        if lotto_value in win_nums:
            i += 1
            
    return rank_dict[count_zero + i],rank_dict[i]
